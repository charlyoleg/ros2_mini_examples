=============================
Notes on py_simple_publishing
=============================


Presentation
============

This python-node publish a standard message to the topic /tralala.


Getting started
===============

In a first console::

  cd ros2_mini_examples_ws
  source /opt/ros/dashing/setup.bash
  source install/setup.bash
  ros2 run py_simple_publishing publish_on_tralala


In a second console::

  source /opt/ros/dashing/setup.bash
  ros2 node list
  ros2 topic list
  ros2 topic echo /tralala


