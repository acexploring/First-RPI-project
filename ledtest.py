import RPi.GPIO as GPIO
import time

# Set up the GPIO pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

# Define Morse code for "HELP"
morse_code = {
    "H": "....",  # 4 dots
    "E": ".",     # 1 dot
    "L": ".-..",  # dot-dash-dot-dot
    "P": ".--."   # dot-dash-dash-dot
}

# Function to blink the LED for a dot or dash
def blink_dot():
    GPIO.output(11, 1)  # Turn LED on
    time.sleep(0.2)     # Dot duration
    GPIO.output(11, 0)  # Turn LED off
    time.sleep(0.2)     # Pause between signals

def blink_dash():
    GPIO.output(11, 1)  # Turn LED on
    time.sleep(0.6)     # Dash duration (3x dot duration)
    GPIO.output(11, 0)  # Turn LED off
    time.sleep(0.2)     # Pause between signals

# Function to blink a letter in Morse code
def blink_letter(letter):
    for symbol in morse_code[letter]:
        if symbol == ".":
            blink_dot()
        elif symbol == "-":
            blink_dash()
    time.sleep(0.6)  # Pause between letters (3x dot duration)

# Flash the LED in Morse code for "HELP" for 1 minute
start_time = time.time()
while time.time() - start_time < 60:  # Run for 60 seconds
    for letter in "HELP":
        blink_letter(letter)
    time.sleep(1)  # Pause between repetitions of the word

# Clean up GPIO settings
GPIO.cleanup()