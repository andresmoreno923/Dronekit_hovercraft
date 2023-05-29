from dronekit import connect
import socket
import sys
import numpy as np
import time

def conncect_drone(vehicle):
    attitude = np.round(np.rad2deg([vehicle.attitude.roll,vehicle.attitude.pitch,vehicle.attitude.yaw])).astype(int)
    y_axis = vehicle.channels['3'] 
    x_axis = vehicle.channels['4']
    z_axis = vehicle.channels['1'] 
    data = np.array([x_axis,y_axis,z_axis])
    return ','.join(str(x) for x in data)


connection_string = '/dev/ttyS0' 
baud_rate = 57600
#- Connect the UAV
print(">>>> Connecting with the UAV <<<")
vehicle = connect(connection_string, baud= baud_rate, wait_ready=True)
#- wait_ready flag hold the program untill all the parameters are been read (=, not .)
print('vehicle is connected.')
#-- Read information from the autopilot:
#- Version and attributes
vehicle.wait_ready('autopilot_version')
print('Autopilot version: %s'%vehicle.version)

while True:
    data = conncect_drone(vehicle)
    print(data)
    time.sleep(0.5)
            
