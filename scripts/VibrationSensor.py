import RPi.GPIO as GPIO
import time as time

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