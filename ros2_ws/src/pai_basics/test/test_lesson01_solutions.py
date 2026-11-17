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

# Checks the answers to exercises 5 to 7 of lesson 01.
# To check your own answer, put your module's name in place of lesson01_solutions below.

from pai_basics import lesson01_solutions as answers
from pai_basics.beat_tracker import BeatTracker
import pytest


# Exercise 5: period_from_rate

@pytest.mark.parametrize('rate_hz, period_s', [(2.0, 0.5), (10.0, 0.1), (0.5, 2.0)])
def test_period_is_one_over_rate(rate_hz, period_s):
    assert answers.period_from_rate(rate_hz) == pytest.approx(period_s)


@pytest.mark.parametrize('rate_hz', [0.0, -1.0, float('nan'), float('inf')])
def test_bad_rate_is_rejected(rate_hz):
    with pytest.raises(ValueError):
        answers.period_from_rate(rate_hz)


# Exercise 6: loss_ratio

def test_no_beats_means_no_loss():
    assert answers.loss_ratio(BeatTracker()) == 0.0


def test_loss_ratio_counts_missed_over_expected():
    tracker = BeatTracker()
    for seq in (0, 1, 2, 5):
        tracker.update(seq)
    # 4 received, 2 missed (3 and 4): 2 of 6 expected beats were lost.
    assert answers.loss_ratio(tracker) == pytest.approx(2 / 6)


def test_no_gap_means_zero_loss():
    tracker = BeatTracker()
    for seq in range(10):
        tracker.update(seq)
    assert answers.loss_ratio(tracker) == 0.0


# Exercise 7: RestartTracker

def test_restart_is_counted_and_is_not_a_gap():
    tracker = answers.RestartTracker()
    for seq in (5, 6, 7, 0, 1):
        tracker.update(seq)
    assert (tracker.restarts, tracker.missed, tracker.received) == (1, 0, 5)


def test_repeated_number_counts_as_restart():
    tracker = answers.RestartTracker()
    tracker.update(3)
    tracker.update(3)
    assert tracker.restarts == 1


def test_first_beat_is_not_a_restart():
    tracker = answers.RestartTracker()
    tracker.update(42)
    assert tracker.restarts == 0


def test_reset_clears_restarts():
    tracker = answers.RestartTracker()
    tracker.update(9)
    tracker.update(0)
    tracker.reset()
    assert (tracker.restarts, tracker.received, tracker.last_seq) == (0, 0, None)


def test_gaps_still_work_after_a_restart():
    tracker = answers.RestartTracker()
    for seq in (8, 9, 0, 3):
        tracker.update(seq)
    assert (tracker.restarts, tracker.missed) == (1, 2)
