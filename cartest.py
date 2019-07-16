import rospy
import time
import sys
import math
import serial
import string

device_port = rospy.get_param('~port', '/dev/stm32base') # device port
baudrate = float( rospy.get_param('~baudrate', '115200') ) # baudrate
# Serial Communication
try:
    serial = serial.Serial(device_port, baudrate, timeout=10)
    rospy.loginfo("Flusing first 50 data readings ...")
    for x in range(0, 50):
        data = serial.read()
        time.sleep(0.01)

except serial.serialutil.SerialException:
    rospy.logerr("Can not receive data from the port: " + device_port + 
    ". Did you specify the correct port ?")
    serial.close
    sys.exit(0) 
    rospy.loginfo("Communication success !")


output = chr(83) + chr(86) + chr(253.3) + chr(253.3) + chr(253.3) + chr(253.3)+chr(69)
#print output     
serial.write(output)