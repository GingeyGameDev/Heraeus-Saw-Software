import time as time

try:
    import RPi.GPIO as GPIO
except (RuntimeError, ModuleNotFoundError):
    import sys
    import fake_rpi

    sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi
    sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO # Fake GPIO
    import RPi.GPIO as GPIO


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