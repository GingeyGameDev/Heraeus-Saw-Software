import time 
import Timer

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

    
#creates a motion sensor object and assignes it to the 17 pin
channel = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN)

#prints "movement detected" when run
def callback(channel):
    if(GPIO.input(channel)):
        print("Movement detected")
    else:
        print("Movement detected")
    
#gives out a signal dependant on whether the pin goes high or low and runs the function if it is high
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime = 300)
GPIO.add_event_callback(channel, callback)

while(True):
    time.sleep(1)
    




#Code that we shall test in the future ---
sensorPin = 11 #check what pin # it is on NOT THE GPIO NUMBER!!!

#sets up the board and the pin that the motion sensor is on
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.SETUP(sensorPin, GPIO.IN, GPIO.PUD_UP)

def test():
    setup()
    while True:
        if GPIO.input(sensorPin) == GPIO.low:
            #time.sleep(3)
            if GPIO.input(sensorPin) == GPIO.low:
                print("Motion Detected!")
            break
        else:
            print("No motion is happening")
        time.sleep(1)

#waits for vibration and returns the system time for a timer when detected. Timer is started 2 seconds late to ensure it does not start in the case of another source of vibration such as walking
def waitForStart():
    while True:
        if GPIO.input(sensorPin) == GPIO.low:
            time.sleep(2)
            if GPIO.input(sensorPin) == GPIO.low:
                return Timer.beginTime()
        else:
            time.sleep(.5)

#waits for the vibration to stop and returns system time. 2 is added because the timer was started 2 seconds late
def stopTime():
    while True:
        if GPIO.input(sensorPin) == GPIO.low:
            time.sleep(.5)
        else:
            return (time.time() + 2)
