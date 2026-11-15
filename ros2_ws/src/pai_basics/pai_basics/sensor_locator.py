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

"""Node that asks tf2 where the sensor is in the map, once per second."""

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.time import Time
from tf2_ros import Buffer, TransformException, TransformListener


class SensorLocator(Node):
    """Look up map -> sensor and log the result."""

    def __init__(self):
        """Start listening to transforms and create the timer."""
        super().__init__('sensor_locator')
        self._buffer = Buffer()
        self._listener = TransformListener(self._buffer, self)
        self.create_timer(1.0, self._report)

    def _report(self):
        try:
            # Time() means "the latest transform available".
            found = self._buffer.lookup_transform('map', 'sensor', Time())
        except TransformException as error:
            self.get_logger().warning(f'No transform yet: {error}')
            return
        position = found.transform.translation
        self.get_logger().info(f'sensor in map: x={position.x:.3f} y={position.y:.3f}')


def main():
    """Run the node until Ctrl+C."""
    rclpy.init()
    node = SensorLocator()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
