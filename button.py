#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys

mypin = int(sys.argv[1])

GPIO.setmode(GPIO.BCM)

GPIO.setup(mypin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(mypin)
    if input_state == False:
        print('Button Pressed')
