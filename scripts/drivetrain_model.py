#!/usr/bin/env python
import rospy
from wpilib.simulation import DifferentialDrivetrainSim
from wpimath.system import *
from wpimath.system.plant import *

class DrivetrainModel():

    def __init__(self):
        pass

if __name__ == '__main__':
    try:
        model = DrivetrainModel
    except rospy.ROSInterruptException:
        pass