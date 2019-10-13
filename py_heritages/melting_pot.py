# melting_pot.py

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

# importing stuff
import publish_on_tralala # from py_simple_publishing



def main(args=None):
  rclpy.init(args=args)

  the_node = publish_on_tralala.PublishOnTralala()

  rclpy.spin(the_node)

  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  the_node.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()

