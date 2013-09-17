# -*- coding: utf-8 -*-
'''
Created on 2013/09/13

@author: kila692
'''

if __name__ == '__main__':
    pass

from SensorADC import sensor

mysensors=[sensor("P9_40"),sensor("P9_39"),sensor("P9_38"),sensor("P9_37"),sensor("P9_36"),sensor("P9_35")]


while 1:
    for i in mysensors:
        print ADC.read("P9_40")
        i.update
        print i.volt,
    print
    



