#!/usr/bin/python
#import gpiozero as gpiozero
#import time as time
#import Timer as Timer

#Makes a limit switch variable taking an input from the pin the button is on
#limitSwitch = gpiozero.Button(11)

#tests every .5 seconds if the switch is being held down, and if it isn't, it will start a timer which will end once the button is pressed down again
"""while True:
  if not limitSwitch.is_held:
    startTime = Timer.beginTime()
    print("switch has been let go")
    while not limitSwitch.is_held:
      time.sleep(.5)
    else:
      time.sleep(.5)
    time.sleep(.5)
  time.sleep(.5)
  """

import RPi.GPIO as GPIO
import time

# Button pin
P_BUTTON = 11 # adapt to your wiring

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN, GPIO.PUD_UP)

setup()
while True:
    while GPIO.input(P_BUTTON) == GPIO.LOW:
        print("Button is held down")
    else:
        print("Button has been let go")
    time.sleep(1)

