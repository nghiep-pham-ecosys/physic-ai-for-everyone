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

from pai_basics.beat_tracker import BeatTracker


def test_consecutive_beats_have_no_gap():
    tracker = BeatTracker()
    assert [tracker.update(seq) for seq in (0, 1, 2)] == [0, 0, 0]
    assert (tracker.received, tracker.missed) == (3, 0)


def test_gap_counts_the_beats_in_between():
    tracker = BeatTracker()
    tracker.update(4)
    assert tracker.update(8) == 3
    assert (tracker.received, tracker.missed) == (2, 3)


def test_publisher_restart_is_not_a_gap():
    tracker = BeatTracker()
    tracker.update(9)
    assert tracker.update(0) == 0
    assert tracker.missed == 0


def test_reset_forgets_everything():
    tracker = BeatTracker()
    tracker.update(1)
    tracker.update(5)
    tracker.reset()
    assert tracker.update(100) == 0
    assert (tracker.received, tracker.missed) == (1, 0)
