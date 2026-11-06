#!/usr/bin/env bash
# Lesson 01 demo: start the launch file, then inspect the running system.
# Fails if any step fails. Needs no GUI.
set -eo pipefail

export ROS_DOMAIN_ID=58
source /opt/ros/jazzy/setup.bash
source ros2_ws/install/setup.bash

setsid ros2 launch pai_basics heartbeat.launch.py rate_hz:=5.0 &
launch_pid=$!
trap 'kill -INT -- "-$launch_pid" 2>/dev/null || true' EXIT

echo "--- 1/4 nodes"
for _ in $(seq 1 30); do
    nodes=$(ros2 node list --no-daemon 2>/dev/null || true)
    if grep -q '^/heartbeat$' <<<"$nodes" && grep -q '^/monitor$' <<<"$nodes"; then break; fi
    sleep 1
done
echo "$nodes"
grep -q '^/heartbeat$' <<<"$nodes"
grep -q '^/monitor$' <<<"$nodes"

echo "--- 2/4 topic"
timeout 30 ros2 topic echo --once /heartbeat std_msgs/msg/UInt32

echo "--- 3/4 parameter"
# A fresh ros2 command can start before discovery has found the node, so retry.
for _ in $(seq 1 30); do
    rate=$(ros2 param get /heartbeat rate_hz 2>/dev/null || true)
    if grep -q '5\.0' <<<"$rate"; then break; fi
    sleep 1
done
echo "$rate"
grep -q '5\.0' <<<"$rate"

echo "--- 4/4 service"
reply=$(timeout 30 ros2 service call /monitor/reset std_srvs/srv/Trigger)
echo "$reply"
grep -q 'success=True' <<<"$reply"

echo "PASS: lesson 01"
