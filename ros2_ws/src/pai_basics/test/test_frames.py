# Copyright 2026 Nghiep Pham
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import signal
import subprocess
import time

import numpy as np
from pai_basics.rigid2d import quaternion_to_yaw, transform
import pytest
import rclpy
from rclpy.time import Time
from tf2_ros import Buffer, TransformListener

# Own domain so that this test cannot hear other ROS 2 nodes on the machine.
DOMAIN_ID = 62
TIMEOUT_S = 30.0


def _matrix(stamped):
    motion = stamped.transform
    yaw = quaternion_to_yaw(motion.rotation.z, motion.rotation.w)
    return transform(motion.translation.x, motion.translation.y, yaw)


def test_tf2_agrees_with_composing_the_matrices_by_hand():
    launch = subprocess.Popen(
        ['ros2', 'launch', 'pai_basics', 'frames.launch.py'],
        env=dict(os.environ, ROS_DOMAIN_ID=str(DOMAIN_ID)),
        start_new_session=True,
    )
    rclpy.init(domain_id=DOMAIN_ID)
    node = rclpy.create_node('test_client')
    buffer = Buffer()
    listener = TransformListener(buffer, node)
    try:
        deadline = time.monotonic() + TIMEOUT_S
        while time.monotonic() < deadline:
            rclpy.spin_once(node, timeout_sec=0.1)
            if buffer.can_transform('map', 'sensor', Time()):
                break
        whole = buffer.lookup_transform('map', 'sensor', Time())

        stamp = Time.from_msg(whole.header.stamp)
        steps = [('map', 'odom'), ('odom', 'base_link'), ('base_link', 'sensor')]
        by_hand = np.eye(3)
        for parent, child in steps:
            by_hand = by_hand @ _matrix(buffer.lookup_transform(parent, child, stamp))

        assert np.allclose(by_hand, _matrix(whole), atol=1e-6)
        assert np.linalg.norm(by_hand[:2, 2] - [2.0, 0.0]) == pytest.approx(
            np.hypot(1.0, 0.2), abs=1e-6)
    finally:
        del listener
        node.destroy_node()
        rclpy.shutdown()
        os.killpg(launch.pid, signal.SIGINT)
        launch.wait(timeout=TIMEOUT_S)
