#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys

mypin = int(sys.argv[1])

GPIO.setmode(GPIO.BCM)

GPIO.setup(mypin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def flashme:
  iters = 10
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


while True:
  input_state = GPIO.input(mypin)
  if input_state == False:
    print('Button Pressed')
    time.sleep(0.05)
