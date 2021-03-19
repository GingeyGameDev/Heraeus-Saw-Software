import time
import Timer


#pattern for switching between RPis
try:
    import sys
    import RPi
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
P_BUTTON = 7 # adapt to your wiring

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

