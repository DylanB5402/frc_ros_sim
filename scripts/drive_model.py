#!/usr/bin/env python
import rospy
from wpilib.simulation import DifferentialDrivetrainSim
from wpimath.system import *
from wpimath.system.plant import *


def run_model():
    rospy.init_node('drivetrain_model', anonymous=True)
    kV = 1.98
    kA = 0.2
    kAngularV = 1.5
    kAngularA = 0.3
    kDriveGearbox = DCMotor.CIM(2)
    kGearing = 8
    kTrackWidth = 0.69
    kWheelDiam = 0.15
    dt = 0.1
    rate = rospy.Rate(dt ** -1)
    kDrivetrainPlant = LinearSystemId.identifyDrivetrainSystem(kV, kA, kAngularV, kAngularA)
    d = DifferentialDrivetrainSim(kDrivetrainPlant, kTrackWidth, kDriveGearbox, kGearing, kWheelDiam/2, )
    left_voltage = 0
    right_voltage = 0
    left_motor_port = '0'
    right_motor_port = '2'
    while not rospy.is_shutdown():
        left_voltage = 0
        right_voltage = 0
        d.setInputs(left_voltage, right_voltage)
        d.update(dt)
        rate.sleep()

class DriveModel:

    def __init__(self):
        rospy.init_node('drivetrain_model', anonymous=True)
        # self.velocity_publisher = 
        kV = 1.98
        kA = 0.2
        kAngularV = 1.5
        kAngularA = 0.3
        kDriveGearbox = DCMotor.CIM(2)
        kGearing = 8
        kTrackWidth = 0.69
        kWheelDiam = 0.15
        dt = 0.1
        rate = rospy.Rate(dt ** -1)
        kDrivetrainPlant = LinearSystemId.identifyDrivetrainSystem(kV, kA, kAngularV, kAngularA)
        self.simModel = DifferentialDrivetrainSim(kDrivetrainPlant, kTrackWidth, kDriveGearbox, kGearing, kWheelDiam/2, )
        self.left_voltage = 0
        self.right_voltage = 0
        self.left_motor_port = '0'
        self.right_motor_port = '2'
        rospy.spin()

    def run(self):
        pass


if __name__ == '__main__':
    try:
        run_model()
    except rospy.ROSInterruptException:
        pass