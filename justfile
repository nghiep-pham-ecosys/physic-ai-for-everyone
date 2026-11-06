# Physical AI for Everyone — the only task runner (ADR-4).
# Run inside the devcontainer (docker/Dockerfile), where ROS 2 Jazzy is installed.

set shell := ["bash", "-eo", "pipefail", "-c"]

ws := "ros2_ws"
ros_setup := "source /opt/ros/jazzy/setup.bash"

# List available recipes
default:
    @just --list

# Build the ROS 2 workspace
build:
    {{ros_setup}} && cd {{ws}} && colcon build --symlink-install

# Build, run all tests, and fail if any test failed
test: build
    {{ros_setup}} && cd {{ws}} && colcon test --event-handlers console_direct+ && colcon test-result --verbose

# Run lesson NN headless (e.g. `just lesson 01`)
lesson NN:
    #!/usr/bin/env bash
    set -eo pipefail
    shopt -s nullglob
    dirs=(lessons/{{NN}}-*/)
    if [ ${#dirs[@]} -eq 0 ]; then
        echo "error: lesson {{NN}} does not exist yet (no lessons/{{NN}}-*/ directory)." >&2
        exit 1
    fi
    if [ ! -f "${dirs[0]}run.sh" ]; then
        echo "error: ${dirs[0]}run.sh does not exist." >&2
        exit 1
    fi
    just build
    bash "${dirs[0]}run.sh"

# Remove colcon build, install and log directories
clean:
    rm -rf {{ws}}/build {{ws}}/install {{ws}}/log

# Run the Starlight site dev server (http://localhost:4321)
site-dev:
    cd site && ([ -d node_modules ] || npm ci) && npm run dev -- --host

# Build the Starlight site; fails on broken internal links
site-build:
    cd site && npm ci && npm run build
