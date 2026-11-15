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

import math

import numpy as np
from pai_basics.rigid2d import apply, invert, quaternion_to_yaw, transform, yaw_to_quaternion
import pytest


def test_identity_changes_nothing():
    assert apply(transform(0.0, 0.0, 0.0), (3.0, 4.0)) == pytest.approx((3.0, 4.0))


def test_translation_moves_a_point():
    assert apply(transform(1.0, 2.0, 0.0), (3.0, 4.0)) == pytest.approx((4.0, 6.0))


def test_quarter_turn_maps_x_to_y():
    assert apply(transform(0.0, 0.0, math.pi / 2.0), (1.0, 0.0)) == pytest.approx((0.0, 1.0))


def test_order_of_composition_matters():
    move = transform(1.0, 0.0, 0.0)
    turn = transform(0.0, 0.0, math.pi / 2.0)
    assert apply(move @ turn, (0.0, 0.0)) == pytest.approx((1.0, 0.0))
    assert apply(turn @ move, (0.0, 0.0)) == pytest.approx((0.0, 1.0))


def test_invert_undoes_a_transform():
    matrix = transform(1.5, -2.0, 0.7)
    assert np.allclose(matrix @ invert(matrix), np.eye(3))


@pytest.mark.parametrize('yaw', [0.0, 0.5, -1.2, 3.0])
def test_quaternion_round_trip(yaw):
    z, w = yaw_to_quaternion(yaw)
    assert quaternion_to_yaw(z, w) == pytest.approx(yaw)
    assert z ** 2 + w ** 2 == pytest.approx(1.0)
