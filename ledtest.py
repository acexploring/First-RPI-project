import RPi.GPIO as GPIO
import time

# Set up the GPIO pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

# Flash the LED for 1 minute
start_time = time.time()
while time.time() - start_time < 60:  # Run for 60 seconds
    GPIO.output(11, 1)  # Turn LED on
    time.sleep(1)     # Wait 0.5 seconds
    GPIO.output(11, 0)  # Turn LED off
    time.sleep(1)     # Wait 0.5 seconds

# Clean up GPIO settings
GPIO.cleanup()