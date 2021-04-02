#!/usr/bin/env python
import rospy
from wpilib.simulation import DifferentialDrivetrainSim
from wpimath.system import *
from wpimath.system.plant import *
import websocket
from std_msgs.msg import Float64MultiArray

import json

def run_model():
    rospy.init_node('wpilib_ws_interface', anonymous=True)
    vel_publisher = rospy.Publisher("drive_vel", Float64MultiArray, queue_size=10)
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:3300/wpilibws")
    left_motor_port = '0'
    right_motor_port = '2'
    left_voltage = 0
    right_voltage = 0
    left_vel = 0
    right_vel = 0
    while not rospy.is_shutdown():
        vel = Float64MultiArray()
        if (ws.connected):
            data = json.loads(ws.recv())
            # rospy.loginfo(data['type'])
            if (data['device'] == 'DriveData'):
                # rospy.loginfo(data['data'])
                # if '<speed' in dict(data['data']).keys():
                #     if (data['device'] == left_motor_port):
                #         left_voltage = 12 * float(data['data']['<speed'])
                #     elif (data['device'] == right_motor_port):
                #         right_voltage = 12 * float(data['data']['<speed'])
                if ('>left_vel_mps' in data['data']):
                    left_vel = float(data['data']['>left_vel_mps'])
                elif ('>right_vel_mps' in data['data']):
                    right_vel = float(data['data']['>right_vel_mps'])
        else:
            left_vel = 0
            right_vel = 0
        vel.data = [-left_vel, -right_vel]
        vel_publisher.publish(vel)
    
    ws.close()
        
        
        


if __name__ == '__main__':
    try:
        run_model()
    except rospy.ROSInterruptException:
        pass