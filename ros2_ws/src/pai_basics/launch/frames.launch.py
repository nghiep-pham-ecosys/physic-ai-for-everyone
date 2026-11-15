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

"""Start the frame tree: map -> odom -> base_link -> sensor."""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """Describe two static transforms and the two lesson nodes."""
    return LaunchDescription([
        # Static transforms. These numbers are teaching values, not robot dimensions.
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='map_to_odom',
            arguments=['--x', '2.0', '--frame-id', 'map', '--child-frame-id', 'odom'],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_to_sensor',
            arguments=[
                '--x', '0.2', '--frame-id', 'base_link', '--child-frame-id', 'sensor'],
        ),
        Node(package='pai_basics', executable='circle_broadcaster'),
        Node(package='pai_basics', executable='sensor_locator'),
    ])
