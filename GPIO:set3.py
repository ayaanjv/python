import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup([25,16,24],GPIO.OUT)

p=GPIO.PWM(25,50)
p.start(50)
##for blink in range(0,101,5):
##    p.start(blink)
##    print(blink)
##    time.sleep(1)
##for loop in range(1,101,10):
##    p.ChangeFrequency(loop)
##    print (loop)
##    time.sleep(10)
##    
y=GPIO.PWM(16,25)
y.start(50)
r=GPIO.PWM(24,12.5)
r.start(50)
time.sleep(10)
##p.ChangeFrequency(0.04)
