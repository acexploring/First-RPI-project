import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)  # Light 1 Red
GPIO.setup(13, GPIO.OUT)  # Light 1 Yellow
GPIO.setup(15, GPIO.OUT)  # Light 1 Green
GPIO.setup(29, GPIO.OUT)  # Light 2 Red
GPIO.setup(31, GPIO.OUT)  # Light 2 Yellow
GPIO.setup(37, GPIO.OUT)  # Light 2 Green
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button for Light 1
GPIO.setup(18, GPIO.IN)  # Button for Light 2

def traffic_light_cycle():
    # Step 1: Light 1 Green, Light 2 Red
    GPIO.output(15, 1)  # Light 1 Green ON
    GPIO.output(29, 1)  # Light 2 Red ON
    time.sleep(15)
    GPIO.output(15, 0)  # Light 1 Green OFF

    # Step 2: Light 1 Yellow, Light 2 Red
    GPIO.output(13, 1)  # Light 1 Yellow ON
    time.sleep(3)
    GPIO.output(13, 0)  # Light 1 Yellow OFF

    # Step 3: Light 1 Red, Light 2 Green
    GPIO.output(11, 1)  # Light 1 Red ON
    GPIO.output(37, 1)  # Light 2 Green ON
    GPIO.output(29, 0)  # Light 2 Red OFF

    # Check for button press during red light
    red_light_duration = 15  # Default red light duration
    start_time = time.time()
    button_pressed = False  # Flag to track if the button has been pressed

    while time.time() - start_time < red_light_duration:
        if GPIO.input(16) == GPIO.LOW and not button_pressed:  # Button pressed (active low) and not already handled
            red_light_duration = 5  # Reduce red light duration to 5 seconds
            button_pressed = True  # Set the flag to prevent further reductions
        time.sleep(0.1)  # Small delay to avoid busy-waiting

    GPIO.output(37, 0)  # Light 2 Green OFF

    # Step 4: Light 1 Red, Light 2 Yellow
    GPIO.output(31, 1)  # Light 2 Yellow ON
    time.sleep(3)
    GPIO.output(31, 0)  # Light 2 Yellow OFF
    GPIO.output(11, 0)  # Light 1 Red OFF

try:
    while True:
        traffic_light_cycle()
except KeyboardInterrupt:
    GPIO.cleanup()


