import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

try: 
    while True:
        blink_count = int(input("How many times should the LED blink? "))
        for i in range(blink_count):
            GPIO.output(11, 1)
            time.sleep(0.5)
            GPIO.output(11, 0)
            time.sleep(0.5)
        repeat = input("Do you want to blink the LED again? (y/n) ")
        if repeat.lower() != "y":
            break
except KeyboardInterrupt:
    GPIO.cleanup()