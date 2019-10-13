# simplet_x.py

import rclpy
from rclpy.node import Node



class SimpletX(Node):

  def __init__(self):
    super().__init__('simplet_x')
    timer_period = 0.5  # seconds
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0

  def timer_callback(self):
    msg = 'simplet_x sings: {:d}'.format(self.i)
    self.get_logger().info('Singing: "{:s}"'.format(msg))
    self.i += 1


def main(args=None):
  rclpy.init(args=args)

  the_node = SimpletX()

  rclpy.spin(the_node)

  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  the_node.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()

