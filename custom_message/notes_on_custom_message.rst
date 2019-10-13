=======================
Notes on custom_message
=======================


Presentation
============

This ros2-package declares a custom message *Billet*.


Getting started
===============

In a first console::

  cd ros2_mini_examples_ws
  source /opt/ros/dashing/setup.bash
  source install/setup.bash
  ros2 msg list | grep Billet
  ros2 msg show custom_message/msg/Billet
  ros2 msg show custom_message/Billet
  ros2 topic pub /trilili custom_message/msg/Billet "{value: '50', serial_number: '12345678', owner: 'Picsous'}"
  ros2 topic pub /trilili custom_message/Billet "{value: '50', serial_number: '12345678', owner: 'Picsous'}"


In a second console::

  source /opt/ros/dashing/setup.bash
  cd ros2_mini_examples_ws
  source install/setup.bash
  ros2 node list
  ros2 topic list
  ros2 topic echo /trilili


Observations
============

- The name of the message must start with a Capital letter (e.g: Billet.msg)
- When using a message-path, /msg/ is optional (e.g: custom_message/msg/Billet and custom_message/Billet are equivalent)
- Custom messages can currently only be created by ament_cmake package (i.e. not with ament_python)

