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

"""Node that publishes a counter on the `heartbeat` topic at a fixed rate."""

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import UInt32


class Heartbeat(Node):
    """Publish an increasing counter so that others can see this node is alive."""

    def __init__(self):
        """Read the `rate_hz` parameter and start the publishing timer."""
        super().__init__('heartbeat')
        self.declare_parameter('rate_hz', 2.0)
        rate_hz = self.get_parameter('rate_hz').value
        self._publisher = self.create_publisher(UInt32, 'heartbeat', 10)
        self._seq = 0
        self.create_timer(1.0 / rate_hz, self._beat)
        self.get_logger().info(f'Publishing at {rate_hz} Hz')

    def _beat(self):
        msg = UInt32()
        msg.data = self._seq
        self._publisher.publish(msg)
        self._seq += 1


def main():
    """Run the node until Ctrl+C."""
    rclpy.init()
    node = Heartbeat()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
