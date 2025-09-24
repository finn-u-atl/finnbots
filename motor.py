import RPi.GPIO as GPIO
import time

# Pin Definitions
IN1 = 22  # GPIO pin connected to IN1 on the L298N
IN2 = 27  # GPIO pin connected to IN2 on the L298N
ENA = 17  # GPIO pin connected to ENA on the L298N (for PWM)

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

# Initialize PWM on ENA pin with 100Hz frequency
pwm = GPIO.PWM(ENA, 100)
pwm.start(0)  # Start with 0% duty cycle (motor off)

def motor_forward(speed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(speed)  # Set speed (0 to 100)

def motor_backward(speed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm.ChangeDutyCycle(speed)  # Set speed (0 to 100)

def motor_stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)  # Set speed to 0%

try:
    while True:
        print('going forward 50')
        motor_forward(50)  # Motor forward at 50% speed
        time.sleep(2)      # Run for 2 seconds
        motor_stop()
        time.sleep(1)      # Stop for 1 second
        print('going backward 50')
        motor_backward(75) # Motor backward at 75% speed
        time.sleep(2)      # Run for 2 seconds
        motor_stop()
        time.sleep(1)      # Stop for 1 second

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()  # Clean up the GPIO pins

finally:
    pwm.stop()
    GPIO.cleanup()  # Clean up the GPIO pins
