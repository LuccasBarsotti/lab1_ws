#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDrive


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            AckermannDrive,
            'drive',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(AckermannDrive, 'drive_relay', 10)

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: v= {msg.speed:.2f} and d= {msg.steering_angle:.2f}')

        new_msg= AckermannDrive()
        new_msg.speed = 3*msg.speed
        new_msg.steering_angle= 3*msg.steering_angle

        self.publisher_.publish(new_msg)
        self.get_logger().info(f'Published Speed: {new_msg.speed:.2f} and steering angle: {new_msg.steering_angle:.2f}')


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()