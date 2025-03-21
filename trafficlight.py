import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT) #red traffic light
GPIO.setup(13, GPIO.OUT) #yellow traffic light
GPIO.setup(15, GPIO.OUT) #green traffic light
GPIO.setup(29, GPIO.OUT) #second red traffic light
GPIO.setup(31, GPIO.OUT) #second yellow traffic light
GPIO.setup(37, GPIO.OUT) #second green traffic light
GPIO.setup(16, GPIO.IN) #button for light number 1
GPIO.setup(18, GPIO.IN) #button for light number 2

def traffic_light_cycle():
    # Step 1: Light 1 Green, Light 2 Red
    GPIO.output(15, 1)  # Light 1 Green ON
    GPIO.output(29, 1)  # Light 2 Red ON
    time.sleep(10)
    GPIO.output(15, 0)  # Light 1 Green OFF

    # Step 2: Light 1 Yellow, Light 2 Red
    GPIO.output(13, 1)  # Light 1 Yellow ON
    time.sleep(2)
    GPIO.output(13, 0)  # Light 1 Yellow OFF

    # Step 3: Light 1 Red, Light 2 Green
    GPIO.output(11, 1)  # Light 1 Red ON
    GPIO.output(37, 1)  # Light 2 Green ON
    GPIO.output(29, 0)  # Light 2 Red OFF
    time.sleep(10)
    GPIO.output(37, 0)  # Light 2 Green OFF

    # Step 4: Light 1 Red, Light 2 Yellow
    GPIO.output(31, 1)  # Light 2 Yellow ON
    time.sleep(2)
    GPIO.output(31, 0)  # Light 2 Yellow OFF
    GPIO.output(11, 0)  # Light 1 Red OFF

try:
    while 1>0:
        traffic_light_cycle()
except KeyboardInterrupt:
    GPIO.cleanup()


    