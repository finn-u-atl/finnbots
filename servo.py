import RPi.GPIO as GPIO
from time import sleep

# Use BCM GPIO numbering
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
pwm=GPIO.PWM(18, 50)
pwm.start(0)

def setAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(18, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    pwm.ChangeDutyCycle(duty)

setAngle(0)
setAngle(50)
setAngle(90)
setAngle(0)
setAngle(90)
GPIO.cleanup()
