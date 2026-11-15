#!/usr/bin/env bash
# Lesson 02 demo: start the frame tree, then inspect it.
# Fails if any step fails. Needs no GUI.
set -eo pipefail

export ROS_DOMAIN_ID=63
source /opt/ros/jazzy/setup.bash
source ros2_ws/install/setup.bash

log=$(mktemp)
setsid ros2 launch pai_basics frames.launch.py >"$log" 2>&1 &
launch_pid=$!
trap 'kill -INT -- "-$launch_pid" 2>/dev/null || true' EXIT

echo "--- 1/4 tree"
tree=$(cd "$(mktemp -d)" && timeout 30 ros2 run tf2_tools view_frames 2>&1)
for frame in map odom base_link sensor; do
    grep -q "$frame" <<<"$tree"
    echo "found frame: $frame"
done

echo "--- 2/4 static transform base_link -> sensor"
fixed=$(timeout 6 stdbuf -oL ros2 run tf2_ros tf2_echo base_link sensor 2>&1 || true)
grep -m1 'Translation' <<<"$fixed"
grep -q 'Translation: \[0.200, 0.000, 0.000\]' <<<"$fixed"

echo "--- 3/4 dynamic transform odom -> base_link"
moving=$(timeout 6 stdbuf -oL ros2 run tf2_ros tf2_echo odom base_link 2>&1 || true)
grep 'Translation' <<<"$moving" | head -3
[ "$(grep 'Translation' <<<"$moving" | sort -u | wc -l)" -ge 2 ]

echo "--- 4/4 sensor in map"
for _ in $(seq 1 15); do
    if grep -q 'sensor in map' "$log"; then break; fi
    sleep 1
done
grep -m1 'sensor in map' "$log" | sed 's/.*\]: //'

echo "PASS: lesson 02"
