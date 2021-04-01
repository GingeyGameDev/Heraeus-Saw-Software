from time import sleep 
import Timer
import RPi.GPIO as GPIO

#method for switching between RPis
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

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

vibr_pin = 11
GPIO.setup(vibr_pin, GPIO.IN)

def waitForStart():
    while True:
        if(GPIO.input(vibr_pin) == 1):
            print("Motion Detected")
            return Timer.beginTime()
            break
        else:
            sleep(1)
    
def stopTiming(startTime):
    while True:
        if(not GPIO.input(vibr_pin) == 1):
            print("Motion has stopped")
            return finishTime(startTime)
        else:
            sleep(1)