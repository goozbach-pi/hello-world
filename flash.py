#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys


print sys.argv


pinNum = int(sys.argv[1])

iters = 10

print pinNum

GPIO.setmode(GPIO.BCM) #numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(pinNum,GPIO.OUT) #replace pinNum with whatever pin you used, this sets up that pin as an output
#set LED to flash forever

for i in range(1,iters):
  print "hi"
  GPIO.output(pinNum,GPIO.HIGH)
  time.sleep(0.5)
  print "low"
  GPIO.output(pinNum,GPIO.LOW)
  time.sleep(0.5)
