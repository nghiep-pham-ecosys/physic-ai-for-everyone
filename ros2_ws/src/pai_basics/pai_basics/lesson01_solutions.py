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

"""Answers to the code exercises 5 to 7 of lesson 01 (no ROS needed)."""

import math

from pai_basics.beat_tracker import BeatTracker


def period_from_rate(rate_hz):
    """Return the timer period in seconds for `rate_hz`, or raise ValueError."""
    # Exercise 5. `not rate_hz > 0` is also true for NaN, unlike `rate_hz <= 0`.
    if not rate_hz > 0 or math.isinf(rate_hz):
        raise ValueError(f'rate_hz must be a positive finite number, got {rate_hz}')
    return 1.0 / rate_hz


def loss_ratio(tracker):
    """Return the share of beats that `tracker` expected but did not receive."""
    # Exercise 6. Every beat was either received or missed.
    expected = tracker.received + tracker.missed
    if expected == 0:
        return 0.0
    return tracker.missed / expected


class RestartTracker(BeatTracker):
    """A BeatTracker that also counts how often the publisher restarted."""

    def reset(self):
        """Forget everything seen so far, restarts included."""
        # Exercise 7. BeatTracker.__init__ calls reset(), so this also
        # creates the counter.
        super().reset()
        self.restarts = 0

    def update(self, seq):
        """Record beat `seq`, count a restart if needed, and return the gap."""
        # Check before super().update(), which overwrites last_seq.
        if self.last_seq is not None and seq <= self.last_seq:
            self.restarts += 1
        return super().update(seq)
