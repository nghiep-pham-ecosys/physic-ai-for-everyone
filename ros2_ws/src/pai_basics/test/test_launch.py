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

import rclpy
from std_msgs.msg import UInt32
from std_srvs.srv import Trigger

# Own domain so that this test cannot hear other ROS 2 nodes on the machine.
DOMAIN_ID = 57
TIMEOUT_S = 30.0


def _spin_until(node, condition):
    deadline = time.monotonic() + TIMEOUT_S
    while not condition() and time.monotonic() < deadline:
        rclpy.spin_once(node, timeout_sec=0.1)
    return condition()


def test_launch_file_starts_both_nodes():
    launch = subprocess.Popen(
        ['ros2', 'launch', 'pai_basics', 'heartbeat.launch.py', 'rate_hz:=20.0'],
        env=dict(os.environ, ROS_DOMAIN_ID=str(DOMAIN_ID)),
        start_new_session=True,
    )
    rclpy.init(domain_id=DOMAIN_ID)
    node = rclpy.create_node('test_client')
    try:
        beats = []
        node.create_subscription(UInt32, 'heartbeat', lambda msg: beats.append(msg.data), 10)
        assert _spin_until(node, lambda: len(beats) >= 5), 'no heartbeat received'
        assert all(b > a for a, b in zip(beats, beats[1:])), f'not increasing: {beats}'

        client = node.create_client(Trigger, 'monitor/reset')
        assert client.wait_for_service(timeout_sec=TIMEOUT_S), 'no reset service'
        future = client.call_async(Trigger.Request())
        assert _spin_until(node, future.done), 'reset service did not answer'
        assert future.result().success
        assert future.result().message.startswith('received=')
    finally:
        node.destroy_node()
        rclpy.shutdown()
        os.killpg(launch.pid, signal.SIGINT)
        launch.wait(timeout=TIMEOUT_S)
