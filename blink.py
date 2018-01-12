import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
print("Setup complete.")
while True:
    sleep(1)
    GPIO.output(18, GPIO.HIGH)
    print("The led is on")
    sleep(1)
    GPIO.output(18, GPIO.LOW)
    print("The led is off")

