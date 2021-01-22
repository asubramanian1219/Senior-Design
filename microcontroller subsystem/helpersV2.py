import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#12,13,18,19
GPIO.setup(12,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
#GPIO.setup(13,GPIO.out)
#GPIO.setup(19,GPIO.out)

#100hz reverse
#66hz stopped
#50hz forward


r=GPIO.PWM(12,100)#forward 100-500 backward 0-10000?
l=GPIO.PWM(18,100)  #left?
#f2=GPIO.PWM(13,100)
#b2=GPIO.PWM(19,100)

def motorsforward():
    r.start(100)
    l.start(100)
    r.ChangeDutyCycle(0)
    l.ChangeDutyCycle(0)
    time.sleep(2)
    r.stop()
    l.stop()
    print('going forward')

def motorsbackward():
    r.start(100)
    l.start(100)
    r.ChangeDutyCycle(100)
    l.ChangeDutyCycle(100)
    time.sleep(3)
    r.stop()
    l.stop()
    print('going backward')

def motorsturnleft():
    r.start(100)
    l.start(100)
    r.ChangeDutyCycle(0)
    l.ChangeDutyCycle(100)
    time.sleep(1.5)
    r.stop()
    l.stop()
    print('turning left')

def motorsturnright():
    r.start(100)
    l.start(100)
    r.ChangeDutyCycle(100)
    l.ChangeDutyCycle(0)
    time.sleep(1.5)
    r.stop()
    l.stop()
    print('turning right')

def motorsturnbackright():
    r.start(100)
    l.start(100)
    r.ChangeDutyCycle(100)
    l.ChangeDutyCycle(70)
    time.sleep(1.5)
    r.stop()
    l.stop()
    print('turning back right')


def motorsturnbackleft():
    r.start(100)
    l.start(100)
    r.ChangeDutyCycle(70)
    l.ChangeDutyCycle(100)
    time.sleep(1.5)
    r.stop()
    l.stop()
    print('turning back left')

def stop():
    r.start(70)
    l.start(70)
    r.ChangeDutyCycle(70)
    l.ChangeDutyCycle(70)
    time.sleep(1)
    r.stop()
    l.stop()
    print('stopping')