#!/usr/bin/python3.5
import serial
import time
import microgear.client as microgear
appid=’xxxxxx’       # Application Id
key=’xxxxxxxxxx’ ​    # Application Device Key
secret=’xxxxxxxxxx’ ​ # Application Secret Key
microgear.create(key,secret,appid,{'debugmode': True})
Ser = serial.Serial(‘/dev/ttyS3’, 38400, stopbits=serial.STOPBITS_TWO, timeout=0.002)
While 1:
     ser.setBreak(True) ​ # Break for 1 Second
     time.sleep(1)
     ser.setBreak(False)
     ser.write(serial.to_bytes([ 0x54, 0x00, 0x30, 0x09, 0x00, 0x72 ])) ​ # Sending Hex
     time.sleep(0.07)
     x=ser.readline( ) ​ # Read the response
     y=int.from_bytes(x, byteorder=’big’) ​ # Convert the response to Integer
     print(y)
     microgear.setalias(“board”) ​ # Set Alias
     microgear.publish(“/bbb”, y, {‘retain’: True}) ​ # Publish to topic: bbb
     microgear.connect(True) ​ # Establish connection with NETPIE
