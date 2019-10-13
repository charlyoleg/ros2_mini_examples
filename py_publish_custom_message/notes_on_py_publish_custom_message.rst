==================================
Notes on py_publish_custom_message
==================================


Presentation
============

This python-node publish the custom message *Billet* to the topic */trilili*.


Getting started
===============

In a first console::

  cd ros2_mini_examples_ws
  source /opt/ros/dashing/setup.bash
  source install/setup.bash
  ros2 msg list | grep Billet
  ros2 msg show py_publish_custom_message/msg/Billet
  ros2 topic pub /trilili py_publish_custom_message/msg/Billet "{value: '50', serial_number: '12345678', owner: 'Picsous'}"
  #ros2 run py_simple_publishing publish_on_tralala


In a second console::

  source /opt/ros/dashing/setup.bash
  ros2 node list
  ros2 topic list
  ros2 topic echo /trilili


Observations
============

- The name of the message must start with a Capital letter (e.g: Billet.msg)
- When using a message-path, /msg/ is optional (e.g: py_publish_custom_message/msg/Billet and py_publish_custom_message/Billet are equivalent)
