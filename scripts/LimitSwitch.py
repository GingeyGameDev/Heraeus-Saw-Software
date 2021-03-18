import RPi.GPIO as GPIO
import time
import Timer

# Button pin
P_BUTTON = 7 # adapt to your wiring

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

