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

"""Pure logic that counts received and missed heartbeats (no ROS needed)."""


class BeatTracker:
    """Track heartbeat sequence numbers and count the gaps between them."""

    def __init__(self):
        """Start with no beats seen."""
        self.reset()

    def reset(self):
        """Forget everything seen so far."""
        self.last_seq = None
        self.received = 0
        self.missed = 0

    def update(self, seq):
        """Record beat `seq` and return how many beats were missed before it."""
        gap = 0
        # A lower or equal number means the publisher restarted, not a gap.
        if self.last_seq is not None and seq > self.last_seq:
            gap = seq - self.last_seq - 1
        self.last_seq = seq
        self.received += 1
        self.missed += gap
        return gap
