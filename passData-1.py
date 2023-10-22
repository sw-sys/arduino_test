import time
import serial
# from vpython import *

# object - we can read the arduino data from this
arduinoData = serial.Serial('com5', 115200)

# make computer wait to access the bod(?) port
time.sleep(1)

# loop to repeat py prog and grab data
while True:
    #, if no data, wait and loop
    while (arduinoData.inWaiting()==0):
        pass
    # when data, read it
    dataPacket = arduinoData.readline()
    # change byte data in to str datatype 
    dataPacket = str(dataPacket, 'utf-8')
    # remove/clean data
    dataPacket = dataPacket.strip('\r\n')
    # split on comma, make str array
    splitPacket=dataPacket.split(",")
    # change str array to floats
    x=float(splitPacket[0])
    y=float(splitPacket[1])
    z=float(splitPacket[2])
    # show data being grabbed in this loop
    print("X= ",x,"Y= ",y,"Z= ",z)