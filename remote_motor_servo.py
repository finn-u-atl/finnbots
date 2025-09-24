import RPi.GPIO as GPIO
import time
from evdev import InputDevice, categorize, ecodes
import evdev

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

from evdev import InputDevice, categorize, ecodes
import evdev

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

for device in devices:
    if "Lic Pro" in device.name:
        controller = InputDevice(device.path)
        break

A_BUTTON = 305
B_BUTTON = 304
Y_BUTTON = 306
X_BUTTON = 307
D_UP = {'code':17, 'type': 3, 'value':-1}
D_RIGHT = {'code': 16, 'type': 3, 'value': 1}
D_DOWN = {'code':17, 'type':3, 'value':1}
D_LEFT = {'code':16, 'type':3, 'value':-1}
x_button = False
y_button = False
a_button = False
b_button = False
d_up = False
d_down = False
d_right = False
d_left = False

# Pin Definitions
IN1 = 22  # GPIO pin connected to IN1 on the L298N for motor
IN2 = 27  # GPIO pin connected to IN2 on the L298N for motor
ENA = 17  # GPIO pin connected to ENA on the L298N (for PWM motor)
SERVO_OUT = 18

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)#motor
GPIO.setup(IN2, GPIO.OUT)#motor
GPIO.setup(ENA, GPIO.OUT)#motor
GPIO.setup(SERVO_OUT, GPIO.OUT) #servo

# Initialize PWM on ENA pin with 100Hz frequency
pwm = GPIO.PWM(ENA, 100)
pwm.start(0)  # Start with 0% duty cycle (motor off)

# Initialize PWM on Servo pin with 50Hz frequency
p = GPIO.PWM(18, 50)
p.start(0) # Start with 0% duty cycle (servo off)
angle = 0 # Start the angle at 0, this is 2.5%

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

def angle_to_duty_cycle(angle):
    if angle > 180:
        angle = 180
    elif angle < 0:
        angle = 0
    return (2.5 + (angle / 180) * 10)

def servo_start(angle):
    p.ChangeDutyCycle(angle_to_duty_cycle(angle))

def servo_stop():
    p.ChangeDutyCycle(0)


try:
    while True:
        for event in controller.read_loop():
            if event.type == ecodes.EV_KEY:
                if event.code == x_button:
                    if event.value == 1:
                        x_button = True
                    elif event.value == 0:
                        x_button = False
                elif event.code == y_button:
                    if event.value == 1:
                        y_button = True
                    elif event.value == 0:
                        y_button = False
                elif event.code == b_button:
                    if event.value == 1:
                        b_button = True
                    elif event.value == 0:
                        b_button = False
                elif event.code == a_button:
                    if event.value == 1:
                        a_button = True
                    elif event.value == 0:
                        a_button = False
            if event.code == D_UP['code'] and event.type == D_UP['type']:
                if event.value == D_UP['value']:
                    d_up = True
                    if angle < 180:
                        angle += 90
                    servo_start(angle)
                else:
                    d_up = False
            if event.code == D_DOWN['code'] and event.type == D_DOWN['type']:
                if event.value == D_DOWN['value']:
                    d_down = True
                    if angle > -180:
                        angle -= 90
                    servo_start(angle)
                else:
                    d_down = False
            if event.code == D_LEFT['code'] and event.type == D_LEFT['type']:
                if event.value == D_LEFT['value']:
                    d_left = True
                else:
                    d_left = False
            if event.code == D_RIGHT['code'] and event.type == D_RIGHT['type']:
                if event.value == D_RIGHT['value']:
                    d_right = True
                else:
                    d_right = False
except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    p.stop()
    GPIO.cleanup()  # Clean up the GPIO pins
