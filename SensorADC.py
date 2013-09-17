# -*- coding: utf-8 -*-
'''
Created on 2013/09/14

@author: kila692
'''
import time
import Adafruit_BBIO.ADC as ADC
ADC.setup()
class sensor:
    '''
    Sensor
    '''


    def __init__(self,pinname):
        '''
        Constructor
        '''
        
        self.pinname = pinname
        #ピンの名前
        
        self.volt = 0.00000001
        #電圧値
        self.value = 0
        #どれだけSensorに近いか
        self.floor_volt = 0.00000001
        #床の電圧
        self.line_volt = 1.00000001
        #ラインの電圧l
        self.sabun = 0.00000001
        #差分値
        
    def update(self):
        '''
        Sensor�̒l���擾
        '''
        self.sabun = self.value
        #前の値を一時保管
        
        self.volt = ADC.read(self.pinname)
        time.sleep(0.01)
        self.volt = ADC.read(self.pinname)
        time.sleep(0.01)
        self.value = (self.volt - self.floor_volt)/(self.line_volt - self.floor_volt)
        #ラインに近いか判定
        if self.value > 1:
            self.value = 1
        if self.value < 0:
            self.value = 0
        
        self.sabun = self.sabun - self.value #差分導出

    def vprint(self):
        print self.volt
    
    def lprint(self):
        print self.line_volt

    def fprint(self):
        print self.floor_volt
    
    def lrecord(self):
        self.line_volt = self.volt
    
    def frecord(self):
        self.floor_volt = self.volt        
    
    
if __name__ == "__main__":
    mysensors=[sensor("P9_40"),sensor("P9_33"),sensor("P9_38"),sensor("P9_37"),sensor("P9_36"),sensor("P9_35")]

    print mysensors[0].pinname
    while 1:

        for i in mysensors:
            i.update()
            print i.volt,
        print
    
    
    