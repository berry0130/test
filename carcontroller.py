import rospy
import tf
import time
import sys
import math
import serial
import string

# Get params
device_port = rospy.get_param('~port', '/dev/stm32base') # device port
baudrate = float( rospy.get_param('~baudrate', '115200') ) # baudrate
# Serial Communication
try:
    ser = serial.Serial(self.device_port, self.baudrate, timeout=10)
    rospy.loginfo("Flusing first 50 data readings ...")
    for x in range(0, 50):
        data = self.serial.read()
        time.sleep(0.01)

except serial.serialutil.SerialException:
    rospy.logerr("Can not receive data from the port: "+ self.device_port + 
    ". Did you specify the correct port ?")
    self.serial.close
    sys.exit(0) 
rospy.loginfo("Communication success !")

output = chr(255) + chr(254) + chr(50) + chr(50) + chr(50) + chr(50)+chr(0)+chr(0)+chr(0)
#print output     
self.serial.write(output)