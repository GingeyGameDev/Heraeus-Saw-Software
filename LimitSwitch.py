#!/usr/bin/python
import gpiozero as gpiozero
import time as time
import Timer as Timer

#Makes a limit switch variable taking an input from the pin the button is on
limitSwitch = gpiozero.Button(10)

#tests every .5 seconds if the switch is being held down, and if it isn't, it will start a timer which will end once the button is pressed down again
while True:
  if not limitSwitch.is_held:
    startTime = Timer.beginTime()
    while not limitSwitch.is_held:
      time.sleep(.5)
    else:
      print(Timer.formatTime(Timer.finishTime(startTime)))
  else:
    time.sleep(.5)
  time.sleep(.5)
