#!/usr/bin/env python

import rospy
from rospy import Publisher, Rate 
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray


def tank_drive(leftFrontVel, leftBackVel, rightFrontVel, rightBackVel):
    vel_publisher = Publisher("/robot_drive_controller/command", Float64MultiArray, queue_size=10)
    rospy.init_node("drive_velocity_setpoint", anonymous=True)
    vel_array = Float64MultiArray()
    # left front, left_back, right_front right_back
    vel_array.data = [leftFrontVel, leftBackVel, rightFrontVel, rightBackVel]
    rate = Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo(vel_array)
        vel_publisher.publish(vel_array)
        rate.sleep()

def tank_drive_accel(leftFrontVel, leftBackVel, rightFrontVel, rightBackVel, accel):
    vel_publisher = Publisher("/robot_drive_controller/command", Float64MultiArray, queue_size=10)
    rospy.init_node("drive_velocity_setpoint", anonymous=True)
    vel_array = Float64MultiArray()
    rate = Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo(vel_array)
        vel_publisher.publish(vel_array)
        rate.sleep()

if __name__ == '__main__':
    try:
        tank_drive(15, 15, 15, 15)
    except rospy.ROSInterruptException:
        pass