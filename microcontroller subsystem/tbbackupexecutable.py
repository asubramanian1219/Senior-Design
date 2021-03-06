import RPi.GPIO as GPIO
import time
import helpersV2 as h

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


val=11

if val==1:#go then stop then go
    r.start(100)
    l.start(100)
    time.sleep(4)
    r.ChangeDutyCycle(0)
    l.ChangeDutyCycle(0)
    time.sleep(1)
    r.stop()
    l.stop()
    r.ChangeDutyCycle(100)
    l.ChangeDutyCycle(100)
    time.sleep(1)
    r.stop()
    l.stop()
    time.sleep(1)
    r.start(100)
    l.start(100)
    r.ChangeDutyCycle(0)
    l.ChangeDutyCycle(0)
    time.sleep(1)
    r.ChangeDutyCycle(100)
    l.ChangeDutyCycle(100)
    time.sleep(1)
    r.stop()
    l.stop()
    print('done')

elif (val==10):
    h.stop()
    time.sleep(.05)
    h.stop()
    time.sleep(.05)
    h.stop()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(1)
    h.stop()
    time.sleep(.05)
    h.stop()
    time.sleep(.05)
    h.stop()
    time.sleep(.05)
    h.stop()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(1)
    h.stop()
    time.sleep(.05)
    h.stop()
    time.sleep(.05)
    h.stop()
    time.sleep(.05)
    h.stop()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(1)
    h.stop()
    time.sleep(.05)
    h.stop()
    time.sleep(.05)
    h.stop()
    time.sleep(.05)
    h.stop()
    time.sleep(.05)
    h.stop()
    time.sleep(.05)
    time.sleep(5)

elif (val==2):# go then stop
    print('start')
    h.motorsforward()
    time.sleep(5)
    h.stop()
    time.sleep(.05)
    print('alarm')
    h.stop()
    time.sleep(.05)
    print('alarm')
    h.stop()
    time.sleep(.05)
    print('alarm')
    h.stop()
    time.sleep(.05)
    print('alarm')
    h.stop()
    time.sleep(.05)
    print('alarm')
    h.stop()
    time.sleep(.05)
    print('alarm')
    
    print('done')

elif val==3:#turn right
    print('start')
    h.motorsforward()
    time.sleep(5)
    h.motorsturnright()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(.05)
    h.motorsturnleft()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(3)
    print('done')



elif val==4:#turn left
    print('start')
    h.motorsforward()
    time.sleep(5)
    h.motorsturnleft()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(.05)
    h.motorsturnright()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(3)
    print('done')
    
elif val==5:#right then left
    print('start')
    h.motorsforward()
    time.sleep(5)
    h.motorsturnright()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(.05)
    h.motorsturnleft()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(.05)
    h.motorsturnleft()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(.05)
    h.motorsturnright()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(3)
    print('done')
    
elif val==6:
    print('start')
    h.motorsforward()
    time.sleep(5)
    h.motorsturnleft()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(.05)
    h.motorsturnright()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(.05)
    h.motorsturnright()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(.05)
    h.motorsturnleft()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(3)
    print('done')
    
elif val==7:#open right side
    print('start')
    h.motorsforward()
    time.sleep(5)
    h.motorsbackward()
    time.sleep(.05)
    h.motorsturnright()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(.05)
    h.motorsturnleft()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(.05)
    print('done')


elif val==8:#open left side
    print('start')
    h.motorsforward()
    time.sleep(5)
    h.motorsbackward()
    time.sleep(.05)
    h.motorsturnright()
    time.sleep(.05)
    h.motorsturnbackright()
    time.sleep(.05)
    h.motorsturnleft()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(.05)
    h.motorsturnright()
    time.sleep(.05)
    h.motorsforward()
    time.sleep(.05)
    print('done')

elif val==9:#no open side
    print('start')
    h.motorsforward()
    time.sleep(5)
    h.motorsbackward()
    time.sleep(.05)
    h.motorsturnright()
    time.sleep(.05)
    h.motorsturnbackright()
    time.sleep(.05)
    h.motorsturnleft()
    time.sleep(.05)
    h.motorsturnbackleft()
    time.sleep(.05)
    h.motorsbackward()
    time.sleep(.05)
    h.stop()
    time.sleep(.05)
    print('alarm')
    h.stop()
    time.sleep(.05)
    print('alarm')
    h.stop()
    time.sleep(.05)
    print('alarm')
    h.stop()
    time.sleep(.05)
    print('alarm')
    h.stop()
    print('done')
    
elif val==11:
    print('start')
    h.stop()
    time.sleep(.05)
    print('alarm')
    h.stop()
    time.sleep(.05)
    print('alarm')
    h.stop()
    time.sleep(.05)
    print('alarm')
    h.stop()
    time.sleep(.05)
    print('alarm')
    h.stop()
    time.sleep(.05)
    print('alarm')
    h.stop()
    time.sleep(.05)
    print('alarm')
    print('done')