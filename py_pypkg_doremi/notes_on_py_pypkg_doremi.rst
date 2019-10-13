========================
Notes on py_pypkg_doremi
========================


Presentation
============

This ros2-package contains a python-package.


Getting started
===============

In a first console::

  cd ros2_mini_examples_ws
  source /opt/ros/dashing/setup.bash
  source install/setup.bash
  ros2 run py_pypkg_doremi simplet_x
  ros2 run py_pypkg_doremi simplet_y


In a second console::

  source /opt/ros/dashing/setup.bash
  ros2 node list
  ros2 topic list
  ros2 topic echo /rosout


