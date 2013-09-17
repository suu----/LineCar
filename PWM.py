'''
Created on 2013/09/15

@author: kila692
'''
import Adafruit_BBIO.PWM as PWM
import time

class motor:
    '''
    classdocs
    '''


    def __init__(self,pinname):
        '''
        Constructor
        '''

        self.pinname = pinname
        self.duty = 0
        
        PWM.start(self.pinname, self.duty)

        self.power =0
        
    def accel(self,out):
        self.power = out
        if self.power > 100:
            self.power = 100
        if self.power < 30:
            self.power = 0
        self.duty = self.power
        time.sleep(0.01)
        PWM.set_duty_cycle(self.pinname, self.duty)
        time.sleep(0.01)
    
    def clean(self):
        PWM.stop(self.pinname)
        PWM.cleanup()