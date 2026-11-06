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

"""Node that listens to `heartbeat` and reports beats it did not receive."""

from pai_basics.beat_tracker import BeatTracker
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import UInt32
from std_srvs.srv import Trigger


class Monitor(Node):
    """Count heartbeats and offer a service that clears the counters."""

    def __init__(self):
        """Create the subscription and the `~/reset` service."""
        super().__init__('monitor')
        self._tracker = BeatTracker()
        self.create_subscription(UInt32, 'heartbeat', self._on_beat, 10)
        self.create_service(Trigger, '~/reset', self._on_reset)

    def _on_beat(self, msg):
        gap = self._tracker.update(msg.data)
        if gap > 0:
            self.get_logger().warning(f'Missed {gap} beat(s) before {msg.data}')

    def _on_reset(self, request, response):
        response.message = (
            f'received={self._tracker.received} missed={self._tracker.missed}')
        response.success = True
        self._tracker.reset()
        return response


def main():
    """Run the node until Ctrl+C."""
    rclpy.init()
    node = Monitor()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
