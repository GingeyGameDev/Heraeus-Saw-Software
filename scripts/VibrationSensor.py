import RPi.GPIO as GPIO
import time as time

#creates a motion sensor object and assignes it to the 17 pin
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if(GPIO.input(channel)):
        print("Movement detected")
    else:
        print("Movement detected")
    
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime = 300)
GPIO.add_event_callback(channel, callback)

while(True):
    time.sleep(1)