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
    voltage_publisher = rospy.Publisher("drive_voltage", Float64MultiArray, queue_size=10)
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:3300/wpilibws")
    left_motor_port = '0'
    right_motor_port = '2'
    left_voltage = 0
    right_voltage = 0
    while not rospy.is_shutdown():
        voltage = Float64MultiArray()
        if (ws.connected):
            data = json.loads(ws.recv())
            # rospy.loginfo(data['type'])
            if (data['type'] == 'PWM'):
                # rospy.loginfo(data['data'])
                if '<speed' in dict(data['data']).keys():
                    if (data['device'] == left_motor_port):
                        # print(data['type'], data['device'], data['data']['<speed'])
                        left_voltage = 12 * float(data['data']['<speed'])
                    elif (data['device'] == right_motor_port):
                        right_voltage = -12 * float(data['data']['<speed'])
        else:
            left_voltage = 0
            right_voltage = 0
        voltage.data = [left_voltage, right_voltage]
        voltage_publisher.publish(voltage)
    ws.close()
        
        
        


if __name__ == '__main__':
    try:
        run_model()
    except rospy.ROSInterruptException:
        pass