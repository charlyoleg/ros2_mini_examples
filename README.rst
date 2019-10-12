===========================
Notes on ROS2 mini-examples
===========================


Presentation
============

This repo contains several ROS2 packages to illustrate certain ROS2 functionalities. The main goal of those examples is to learn ROS2.

Prerequisite
============

- Install ROS2 Dashing
- Install colcon


Getting Started
===============

::

  source /opt/ros/dashing/setup.bash
  mkdir -p ros2_mini_examples_ws/src
  cd ros2_mini_examples_ws
  git clone https://github.com/charlyoleg/ros2_mini_examples src/
  colcon build
  source install/setup.bash
  ros2 pkg list

