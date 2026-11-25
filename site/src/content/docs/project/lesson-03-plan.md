---
title: 'Plan: Lesson 03, robot description with URDF'
description: Goals, steps, exercises and CI checks for lesson 03, before any code is written.
---

This page is a plan, not a lesson. It fixes the scope of lesson 03 before code is written. The lesson itself follows the usual four sections: Theory, Terminology, Plain-language explanation and Hands-on.

**Status:** planned. No code exists yet. Simulation (Gazebo) is out of scope and comes in a later P1 lesson ([Roadmap](/physic-ai-for-everyone/project/roadmap/)).

## Goals

After lesson 03 the learner can:

1. Explain what a robot description is: links, joints, and the visual, collision and inertial parts of a link. ([URDF tutorials](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/URDF-Main.html))
2. Name the joint types and say which ones move: `fixed`, `continuous`, `revolute`, `prismatic`, `floating` and `planar`. ([URDF joint](https://wiki.ros.org/urdf/XML/joint))
3. Write a description with xacro: properties, simple math and macros, so that a number is written once. ([Using xacro](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/Using-Xacro-to-Clean-Up-a-URDF-File.html))
4. Publish the description with `robot_state_publisher` and connect it to the TF tree from [Lesson 02](/physic-ai-for-everyone/lessons/02-tf2/). Fixed joints go to `/tf_static` once, and movable joints go to `/tf` when `joint_states` changes. ([robot_state_publisher](https://github.com/ros/robot_state_publisher))
5. Check a description headless: expand it, parse it, and test its tree, with no GUI.

**Prerequisites:** [Lesson 01](/physic-ai-for-everyone/lessons/01-ros2-essentials/) and [Lesson 02](/physic-ai-for-everyone/lessons/02-tf2/). No GPU.

## The robot

The lesson starts `pai_bot`, the project's own robot. The first description is a small wheeled base:

- `base_link` as the root of the robot, as in [REP-105](https://www.ros.org/reps/rep-0105.html);
- two drive wheels on `continuous` joints;
- one caster on a `fixed` joint;
- one sensor mount on a `fixed` joint, with a `sensor` frame like the one in lesson 02.

Frames follow [REP-103](https://www.ros.org/reps/rep-0103.html): x forward, y left, z up, meters and radians.

**Every number is OPEN:** body size, wheel radius, wheel separation, masses and the sensor pose. They need one design decision, recorded before the code, and every value must come from that decision. The plan does not guess them.

## Steps (Hands-on outline)

1. **Run the finished lesson.** `just lesson 03` builds the workspace, starts the description and checks it. It prints `PASS: lesson 03`, or stops with an error.
2. **Read a plain URDF.** One link, then two links and a fixed joint. Show the XML and the frame it creates. ([Building a visual robot model](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/Building-a-Visual-Robot-Model-with-URDF-from-Scratch.html))
3. **Add physical properties.** Collision shapes and inertia, and why a simulator needs them later. ([Adding physical and collision properties](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/Adding-Physical-and-Collision-Properties-to-a-URDF-Model.html))
4. **Clean it up with xacro.** Replace repeated numbers with properties and the two wheels with one macro. Expand the file with the `xacro` command and compare the output.
5. **Publish it.** A launch file passes the expanded description to `robot_state_publisher` through the `robot_description` parameter. ([Using URDF with robot_state_publisher](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/Using-URDF-with-Robot-State-Publisher-py.html))
6. **Make the wheels turn.** A small node publishes `sensor_msgs/msg/JointState` for the two wheel joints. Without it, the wheel frames never appear in the TF tree, because they are movable.
7. **Inspect the tree.** `view_frames` and `tf2_echo`, as in lesson 02. RViz is optional and never needed to pass.

## Exercises

Each exercise has a written answer in `solutions.md`. The ones marked *tested* also get a check that CI runs.

1. **Add a part** *(tested)*. Add a mast link on a fixed joint above the sensor mount. Predict its position in `base_link`, then check it with `tf2_echo`.
2. **Break the tree.** Give a joint a parent link that does not exist, or give one link two parents. Read what `xacro` and `robot_state_publisher` report for each mistake, and find which check in `just test` catches it.
3. **One number, once** *(tested)*. Change the wheel radius in one place only, and show that every part that depends on it moved.

## What runs in CI

All checks run in the existing `ci-ros` job, inside the devcontainer image. Nothing needs a GUI.

| Check | How | Runs in |
| --- | --- | --- |
| The xacro file expands | a test calls `xacro` and fails on any error | `just test` |
| The tree is valid | a test parses the URDF with Python's `xml.etree`: one root, every joint's parent and child exist, no link has two parents | `just test` |
| Inertia is present | every link except the root has an inertial block with a positive mass | `just test` |
| The description is published | a launch test reads `/robot_description` and a fixed transform from `/tf_static` | `just test` |
| The lesson runs | `run.sh` checks the frames with `view_frames`, one fixed transform and one wheel transform | `just lesson 03` |
| The pages build | the English and Vietnamese pages build without broken links | `ci-site` |

`ci-ros.yml` gains `&& just lesson 03` at the end of its command. The tree test uses only the Python standard library, so it needs no new package.

## Decisions to make before the code

| Question | Proposal |
| --- | --- |
| Where the description lives | a new package `pai_description` (`urdf/`, `launch/`, `test/`), so that later lessons and the simulation reuse it |
| Who publishes the joint states | our own small node, rather than adding `joint_state_publisher` to the image; it is short and teaches `JointState` |
| `pai_bot` numbers | one design note; until then, every value is OPEN |

## Out of scope

- Gazebo, the world file and any simulation code.
- Sensors that produce data (camera, lidar). Lesson 03 adds only the frame of the sensor mount.
- Meshes. Lesson 03 uses boxes and cylinders only.

## Done when (lesson 03)

- `just lesson 03` and `just test` pass in `ci-ros`.
- The English page and its Vietnamese translation build in `ci-site`.
- Every number in the description traces back to the design note.
