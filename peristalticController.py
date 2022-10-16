import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#GPIO23
pump = 23

one_oz_ml = 29.5735

# must calculate
ml_per_second = 1

GPIO.setup(pump, GPIO.OUT)

def dispense(ounces):
    mls = ounces * one_oz_ml
    wait_time = mls / ml_per_second
    GPIO.output(pump, GPIO.HIGH)
    time.sleep(wait_time)
    GPIO.output(pump, GPIO.LOW)