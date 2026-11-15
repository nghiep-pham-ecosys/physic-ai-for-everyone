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

"""Rigid transforms in the plane, written with plain matrices (no ROS needed)."""

import math

import numpy as np


def transform(x, y, yaw):
    """Return the 3x3 matrix of a rotation by `yaw` and a translation by (x, y)."""
    cos_yaw, sin_yaw = math.cos(yaw), math.sin(yaw)
    return np.array([
        [cos_yaw, -sin_yaw, x],
        [sin_yaw, cos_yaw, y],
        [0.0, 0.0, 1.0],
    ])


def apply(matrix, point):
    """Return `point` (x, y) expressed in the parent frame of `matrix`."""
    x, y, _ = matrix @ np.array([point[0], point[1], 1.0])
    return float(x), float(y)


def invert(matrix):
    """Return the transform that undoes `matrix`."""
    rotation = matrix[:2, :2]
    translation = matrix[:2, 2]
    result = np.eye(3)
    result[:2, :2] = rotation.T
    result[:2, 2] = -rotation.T @ translation
    return result


def yaw_to_quaternion(yaw):
    """Return (z, w), the non-zero parts of a quaternion that rotates around z."""
    return math.sin(yaw / 2.0), math.cos(yaw / 2.0)


def quaternion_to_yaw(z, w):
    """Return the rotation around z of a quaternion with zero x and y."""
    return 2.0 * math.atan2(z, w)
