import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup([23,25,24,16,20,21],GPIO.OUT)
GPIO.setup(12,GPIO.IN)

signal = 0
while True:
    
    x=GPIO.input(12)
    
    print(x)

    if x==1 and signal ==1:
        GPIO.output([21,23],GPIO.LOW)
        GPIO.output(20,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(20,GPIO.LOW)
        GPIO.output([24,16],GPIO.HIGH)
        signal=0 
    if x==0 and signal ==0:
        GPIO.output([24,16],GPIO.LOW)
        GPIO.output(25,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(25,GPIO.LOW)
        GPIO.output([21,23],GPIO.HIGH)
        signal =1
