# melting_pot.py

import rclpy
from rclpy.node import Node

#from std_msgs.msg import String

# importing stuff
import publish_on_tralala # from py_simple_publishing
import simplet_a # from py_two_modules
#import doremi # from py_pypkg_doremi
import doremi.simplet_x # from py_pypkg_doremi
from custom_message.msg import Billet


class PublishOnTrilili(Node):

  def __init__(self):
    super().__init__('melting_pot_N')
    self.publisher_ = self.create_publisher(Billet, 'trilili', 10)
    timer_period = 0.5  # seconds
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0

  def timer_callback(self):
    msg = Billet()
    msg.value = self.i
    msg.serial_number = 12345
    msg.owner = 'moi'
    self.publisher_.publish(msg)
    self.get_logger().info('Yeh: "%s"' % msg.value)
    self.i += 1


def main(args=None):
  rclpy.init(args=args)

  the_node_1 = publish_on_tralala.PublishOnTralala()
  the_node_2 = simplet_a.SimpletA()
  the_node_3 = doremi.simplet_x.SimpletX()
  the_node_4 = PublishOnTrilili()

  rclpy.spin_once(the_node_1, timeout_sec=3.0)
  rclpy.spin_once(the_node_2, timeout_sec=3.0)
  rclpy.spin_once(the_node_3, timeout_sec=3.0)
  rclpy.spin(the_node_4)

  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  the_node_1.destroy_node()
  the_node_2.destroy_node()
  the_node_3.destroy_node()
  the_node_4.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()

