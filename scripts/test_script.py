#!/usr/bin/env python

import rospy

def test():
    rospy.init_node('test', anonymous=True)
    while not rospy.is_shutdown():
        rospy.loginfo("test")


if __name__ == '__main__':
    try:
        test()
    except rospy.ROSInterruptException:
        pass