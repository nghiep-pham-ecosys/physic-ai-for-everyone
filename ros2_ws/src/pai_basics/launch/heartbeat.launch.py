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

"""Start the heartbeat and monitor nodes together."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    """Describe the two nodes and the `rate_hz` launch argument."""
    rate_hz = ParameterValue(LaunchConfiguration('rate_hz'), value_type=float)
    return LaunchDescription([
        DeclareLaunchArgument('rate_hz', default_value='2.0'),
        Node(
            package='pai_basics',
            executable='heartbeat',
            parameters=[{'rate_hz': rate_hz}],
        ),
        Node(package='pai_basics', executable='monitor'),
    ])
