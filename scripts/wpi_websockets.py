#!/usr/bin/env python
import rospy
from wpilib.simulation import DifferentialDrivetrainSim
from wpimath.system import *
from wpimath.system.plant import *

def test():
    rospy.init_node('test', anonymous=True)
    # while not rospy.is_shutdown():
    #     rospy.loginfo("test")
    kV = 1.98
    kA = 0.2
    kAngularV = 1.5
    kAngularA = 0.3
    kDriveGearbox = DCMotor.CIM(2)
    kGearing = 8
    kTrackWidth = 0.69
    kWheelDiam = 0.15

    kDrivetrainPlant = LinearSystemId.identifyDrivetrainSystem(kV, kA, kAngularV, kAngularA)
    d = DifferentialDrivetrainSim(kDrivetrainPlant, kTrackWidth, kDriveGearbox, kGearing, kWheelDiam/2, )
    rospy.loginfo(d.getLeftVelocity())


if __name__ == '__main__':
    try:
        test()
    except rospy.ROSInterruptException:
        pass