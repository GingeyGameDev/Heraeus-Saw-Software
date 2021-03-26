import time
import Timer


#pattern for switching between RPis
try:
    import sys
    import RPi
    import RPi.GPIO
    sys.modules['RPi'] = RPi
    sys.modules['RPi.GPIO'] = RPi.GPIO
    import RPi.GPIO as GPIO
    
except (RuntimeError, ModuleNotFoundError):
    import sys
    import fake_rpi

    sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi
    sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO # Fake GPIO
    import RPi.GPIO as GPIO

# Button pin
P_BUTTON = 7

#sets up the board mode and the pin to take an input.
def setup():
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(P_BUTTON, GPIO.IN, GPIO.PUD_UP)

setup()
while True:
    while GPIO.input(P_BUTTON) == GPIO.LOW:
        print("Button is held down")
        break
    else:
        print("Button has been let go")
    time.sleep(1)

#Starts a timer when the limit switch is not pressed in and ends it when the switch is pressed in. returns total time the switch was not pressed in(i.e. time the saw was down and cutting)
def timeLogged():
  setup()
  noInput = True
  while noInput:
    if GPIO.input(P_BUTTON) == GPIO.low:
      startTime = Timer.beginTime()
      noInput = False
    else:
      time.sleep(.5)
  while True:
    if not GPIO.input(P_BUTTON) == GPIO.low:
      return Timer.finishTime(startTime)
    else:
      time.sleep(.5)

def determineLimitSwitch():
  while True:
    if GPIO.input(P_BUTTON) == GPIO.low:
     return True
    elif False: #use the method to determine if something new is put in the sheet
      return False
    time.sleep(.5)