# -*- coding: utf-8 -*-
import Adafruit_BBIO.ADC as ADC
ADC.setup()
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM


from SensorADC import sensor
from PWM import motor

import time

mysensors=[sensor("P9_40"),sensor("P9_33"),sensor("P9_38"),sensor("P9_37"),sensor("P9_36"),sensor("P9_35")]

rmotor = motor("P9_14")
lmotor = motor("P9_22")

rpower = 0
lpower = 0

redswich = "P8_11"
whiteswich = "P8_12"
yellowled = 'P8_14'
redled = 'P9_15'

GPIO.setup(redswich, GPIO.IN)#赤スイッチ
GPIO.setup(whiteswich, GPIO.IN)#白スイッチ
GPIO.setup(yellowled, GPIO.OUT)#黄LED
GPIO.setup(redled, GPIO.OUT)#赤LED

GPIO.output(yellowled, GPIO.HIGH)
GPIO.output(redled, GPIO.HIGH)

time.sleep(1.5)
print 'init succes'
'''
初期化完了 LED点灯
'''

'''
線の値読み込み
'''
GPIO.output(yellowled, GPIO.LOW)

while GPIO.input(redswich) == 0:#押されるまで待つ
    pass

GPIO.output(yellowled, GPIO.HIGH)

while GPIO.input(redswich) == 1:#離されるまで待つ

    for i in mysensors:
        i.update()
        print i.volt,
    print

for mysensor in mysensors:
    mysensor.update()
    mysensor.lrecord()

GPIO.output(yellowled, GPIO.HIGH)
print 'line'

'''
床の値読み込み
'''
GPIO.output(redled, GPIO.LOW)

while GPIO.input(whiteswich) == 0:#押されるまで待つ
    pass

GPIO.output(redled, GPIO.HIGH)

while GPIO.input(whiteswich) == 1:#離されるまで待つ
        
    for i in mysensors:
        i.update()
        print i.volt,
    print

print 'floor'

for mysensor in mysensors:
    mysensor.update()
    mysensor.frecord()
    
GPIO.output(redled, GPIO.HIGH)

'''
走行ループ
'''

heikin = 0
while 1:
    sumsen=0.00000001

    for mysensor in mysensors:
     
        mysensor.update()
        sumsen = sumsen + mysensor.value*1000
#         print mysensor.value,

    maeheikin = heikin
    heikin = (mysensors[0].value*1800/sumsen +mysensors[1].value*1200/sumsen + mysensors[2].value*200/sumsen - mysensors[3].value*200/sumsen - mysensors[4].value*1100/sumsen -mysensors[5].value*1800/sumsen)/2
    
    p = heikin
    i = (maeheikin + heikin)/2
    d = (heikin - maeheikin)
    
    rpower = (p * 40 + d *30) + 45
    lpower = -(p * 40 + d *30) + 45
    
    rmotor.accel(rpower)
    lmotor.accel(lpower)
    print p,i,d,lpower,rpower,lmotor.duty,rmotor.duty
    if GPIO.input(redswich) == 1:
        rmotor.clean()
        lmotor.clean()
        GPIO.cleanup()
        exit()
        
