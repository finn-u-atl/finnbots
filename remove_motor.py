import RPi.GPIO as GPIO
import time
from evdev import InputDevice, categorize, ecodes
import evdev

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

for device in devices:
    if "Lic Pro" in device.name:
        controller = InputDevice(device.path)
        print('found controller')
        break

# Button Definitions
A_BUTTON = 305
B_BUTTON = 304
Y_BUTTON = 306
X_BUTTON = 307

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
        for event in controller.read_loop():
            if event.type == ecodes.EV_KEY:
                if event.code == X_BUTTON:
                    if event.value == 1:
                        print('motor should go forward')
                        motor_forward(50)
                    elif event.value == 0:
                        motor_stop()
except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()  # Clean up the GPIO pins
