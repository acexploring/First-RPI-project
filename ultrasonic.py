import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
# Set GPIO pins (using physical pin numbers)
TRIG_PIN = 12  # Pin 12 corresponds to GPIO18 in BOARD mode
ECHO_PIN = 22  # Pin 16 corresponds to GPIO23 in BOARD mode

# Set up the GPIO pins
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def measure_distance():
    # Send a 10us pulse to the TRIG_PIN
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    # Measure the ECHO_PIN pulse duration
    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()
    
    while GPIO.input(ECHO_PIN) == 1:
        stop_time = time.time()

    # Time difference between start and stop
    time_elapsed = stop_time - start_time
    # Calculate distance (speed of sound is ~34300 cm/s)
    distance = (time_elapsed * 34300) / 2
    time.sleep(0.2)
    return distance
try:
    while True:
        distance = measure_distance()
        if distance == -1:
            print("Error: Could not measure distance")
        else:
            print(f"Distance: {distance:.2f} cm")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()