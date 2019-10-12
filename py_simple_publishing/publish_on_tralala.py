# publish_on_tralala.py

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class PublishOnTralala(Node):

    def __init__(self):
        #super().__init__('simple_pub') # you can choose any name for the node
        super().__init__('publish_on_tralala') # but, it is easier that the ros-node-name is identical to the python-module-name
        self.publisher_ = self.create_publisher(String, 'tralala', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    the_node = PublishOnTralala()

    rclpy.spin(the_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    the_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
