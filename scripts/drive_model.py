#!/usr/bin/env python
import rospy
from wpilib.simulation import DifferentialDrivetrainSim
from wpimath.system import *
from wpimath.system.plant import *
from std_msgs.msg import Float64MultiArray



# def run_model():
#     rospy.init_node('drivetrain_model', anonymous=True)
#     kV = 1.98
#     kA = 0.2
#     kAngularV = 1.5
#     kAngularA = 0.3
#     kDriveGearbox = DCMotor.CIM(2)
#     kGearing = 8
#     kTrackWidth = 0.69
#     kWheelDiam = 0.15
#     dt = 0.1
#     rate = rospy.Rate(dt ** -1)
#     kDrivetrainPlant = LinearSystemId.identifyDrivetrainSystem(kV, kA, kAngularV, kAngularA)
#     d = DifferentialDrivetrainSim(kDrivetrainPlant, kTrackWidth, kDriveGearbox, kGearing, kWheelDiam/2, )
#     left_voltage = 0
#     right_voltage = 0
#     left_motor_port = '0'
#     right_motor_port = '2'
#     while not rospy.is_shutdown():
#         left_voltage = 0
#         right_voltage = 0
#         d.setInputs(left_voltage, right_voltage)
#         d.update(dt)
#         rate.sleep()

class DriveModel:

    def __init__(self):
        rospy.init_node('drivetrain_model', anonymous=True)
        self.voltage_subscriber = rospy.Subscriber("/drive_voltage", Float64MultiArray, callback=self.set_velocity)
        self.vel_publisher = rospy.Publisher("/robot_drive_controller/command", Float64MultiArray, queue_size=10)
        kV = 1.98
        kA = 0.2
        kAngularV = 1.5
        kAngularA = 0.3
        kDriveGearbox = DCMotor.CIM(2)
        kGearing = 8
        kTrackWidth = 0.69
        kWheelDiam = 0.1524
        self.wheel_radius = 0.0762
        self.dt = 0.1
        # rate = rospy.Rate(dt ** -1)
        kDrivetrainPlant = LinearSystemId.identifyDrivetrainSystem(kV, kA, kAngularV, kAngularA)
        self.simModel = DifferentialDrivetrainSim(kDrivetrainPlant, kTrackWidth, kDriveGearbox, kGearing, kWheelDiam/2, )
        self.left_voltage = 0
        self.right_voltage = 0
        self.left_motor_port = '0'
        self.right_motor_port = '2'
        rospy.spin()

    def set_velocity(self, voltage):
        voltage_data = voltage.data
        left_voltage = voltage_data[0]
        right_voltage = voltage_data[1]
        self.simModel.setInputs(left_voltage, right_voltage)
        self.simModel.update(self.dt)
        vel_array = Float64MultiArray()
        # divide by radius to convert from m/s to rad/s
        left_vel = self.simModel.getLeftVelocity() / self.wheel_radius
        right_vel = self.simModel.getRightVelocity() / self.wheel_radius
        # left front, left_back, right_front right_back
        vel_array.data = [left_vel, left_vel, right_vel, right_vel]
        self.vel_publisher.publish(vel_array)
        



if __name__ == '__main__':
    try:
        d = DriveModel()
    except rospy.ROSInterruptException:
        pass