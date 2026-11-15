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

"""Node that publishes a moving `base_link` frame, driving in a circle."""

import math

from geometry_msgs.msg import TransformStamped
from pai_basics.rigid2d import yaw_to_quaternion
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from tf2_ros import TransformBroadcaster


class CircleBroadcaster(Node):
    """Publish odom -> base_link for a robot that follows a circle."""

    def __init__(self):
        """Read the circle parameters and start the timer."""
        super().__init__('circle_broadcaster')
        self.declare_parameter('radius', 1.0)
        self.declare_parameter('angular_speed', 0.5)
        self._radius = self.get_parameter('radius').value
        self._angular_speed = self.get_parameter('angular_speed').value
        self._broadcaster = TransformBroadcaster(self)
        self._start = self.get_clock().now()
        self.create_timer(0.05, self._publish)

    def _publish(self):
        now = self.get_clock().now()
        angle = self._angular_speed * (now - self._start).nanoseconds * 1e-9

        msg = TransformStamped()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'odom'
        msg.child_frame_id = 'base_link'
        msg.transform.translation.x = self._radius * math.cos(angle)
        msg.transform.translation.y = self._radius * math.sin(angle)
        # The robot faces along the circle, 90 degrees ahead of its position angle.
        z, w = yaw_to_quaternion(angle + math.pi / 2.0)
        msg.transform.rotation.z = z
        msg.transform.rotation.w = w
        self._broadcaster.sendTransform(msg)


def main():
    """Run the node until Ctrl+C."""
    rclpy.init()
    node = CircleBroadcaster()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
