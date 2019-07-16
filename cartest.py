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

def com_vel(WFR,WFL,WBR,WBL):
# send cmd to motor
    #WFR =  # unit: rad/sec
    #WFL =         
    #WBR = 
    #WBL = 
    WFR_send = WFR  # unit: rad/sec
    WFL_send = WFL 
    WBR_send = WBR
    WBL_send = WBL
    # rospy.loginfo("WR:" + str(WR) + "WL:" + str(WL))
    WFR_send_ba = bytearray(struct.pack("f", WFR_send))  
    WFL_send_ba = bytearray(struct.pack("f", WFL_send))  
    WBR_send_ba = bytearray(struct.pack("f", WBR_send))  
    WBL_send_ba = bytearray(struct.pack("f", WBL_send))  
    # R_forward = 1 # 0: reverse, >0: forward  
        # L_forward = 1 # 0: reverse, >0: forward       
        # if self.WR_send < 0:
        #     R_forward = 0
        #     self.WR_send = -self.WR_send
        # if self.WL_send < 0:
        #     L_forward = 0
        #     self.WL_send = -self.WL_send
        # if self.WR_send > 255:
        #     self.WR_send = 255
        # if self.WL_send > 255:
        #     self.WL_send = 255
    output = [chr(83), chr(86), \
            chr(WFR_send_ba[0]), chr(WFR_send_ba[1]), chr(WFR_send_ba[2]), chr(WFR_send_ba[3]), \
            chr(WFL_send_ba[0]), chr(WFL_send_ba[1]), chr(WFL_send_ba[2]), chr(WFL_send_ba[3]),\
            chr(WBR_send_ba[0]), chr(WBR_send_ba[1]), chr(WBR_send_ba[2]), chr(WBR_send_ba[3]), \
            chr(WBL_send_ba[0]), chr(WBL_send_ba[1]), chr(WBL_send_ba[2]), chr(WBL_send_ba[3]),\
                 chr(69)]
        # output = '0x53' + chr(254) + chr(self.WL_send) + chr(L_forward) + chr(self.WR_send) + chr(R_forward)   
        # print output
        # rospy.loginfo(output)
    serial.write(output)
        # rospy.loginfo("timerCmdCB success !")
for i in range(1,200):
    com_vel(i,i,i,i)
