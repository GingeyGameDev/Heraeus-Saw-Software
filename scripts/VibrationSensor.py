import time as time

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

 """   
#creates a motion sensor object and assignes it to the 17 pin
channel = 17
GPIO.setmode(GPIO.BCM)
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
    """




#Code that we shall test in the future ---
sensorPin = #check what pin # it is on NOT THE GPIO NUMBER!!!

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.SETUP(sensorPin, GPIO.IN, GPIO.PUD_UP)

setup
while True:
    