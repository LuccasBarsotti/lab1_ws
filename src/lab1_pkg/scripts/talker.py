#!/usr/bin/env python3

# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDrive


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('talker_node')
        self.declare_parameter('v', 0.0)
        self.declare_parameter('d', 0.0) 
        self.v= self.get_parameter('v').get_parameter_value().double_value
        self.d= self.get_parameter('d').get_parameter_value().double_value

        self.publisher_ = self.create_publisher(AckermannDrive, 'drive', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = AckermannDrive()
        msg.speed= self.v
        msg.steering_angle= self.d
        self.publisher_.publish(msg)
        self.get_logger().info(f'AAAAAAAAAAAA Publishing Speed: {msg.speed:.2f} and steering angle: {msg.steering_angle:.2f}')
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    talker_node = MinimalPublisher()

    rclpy.spin(talker_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    talker_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
