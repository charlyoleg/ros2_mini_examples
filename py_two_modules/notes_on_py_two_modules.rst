=======================
Notes on py_two_modules
=======================


Presentation
============

This ros2-packages contains two simple python-nodes.


Getting started
===============

In a first console::

  cd ros2_mini_examples_ws
  source /opt/ros/dashing/setup.bash
  source install/setup.bash
  ros2 run py_two_modules simplet_a
  ros2 run py_two_modules simplet_b


In a second console::

  source /opt/ros/dashing/setup.bash
  ros2 node list
  ros2 topic list
  ros2 topic echo /rosout


