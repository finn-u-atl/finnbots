import RPi.GPIO as GPIO
import time

# Use BCM GPIO numbering
GPIO.setmode(GPIO.BCM)

# Set up GPIO 18 as an output
LED_PIN = 20
LED_PIN2 = 21
LED_PIN3 = 13
GPIO.setup(LED_PIN, GPIO.OUT)
#GPIO.setup(LED_PIN2, GPIO.OUT)
#GPIO.setup(LED_PIN3, GPIO.OUT)

try:
    while True:
        # Turn the LED on
        GPIO.output(LED_PIN, GPIO.HIGH)
        #GPIO.output(LED_PIN2, GPIO.LOW)
        #GPIO.output(LED_PIN3, GPIO.HIGH)
        time.sleep(1)  # Wait for 1 second

        # Turn the LED off
        GPIO.output(LED_PIN, GPIO.LOW)
#        GPIO.output(LED_PIN2, GPIO.HIGH)
        time.sleep(1)  # Wait for 1 second
#        GPIO.output(LED_PIN3, GPIO.LOW)
#        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    # Clean up GPIO settings before exiting
    GPIO.cleanup()
