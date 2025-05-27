# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 12:09:36 2021

@author: saira

"""

from math import sin, cos, tan

def MyTan(x): 
    print("MyTan({:.4F}) is {:.4f}".format(x, sin(x) / cos(x)))


AnAngle = float(input("Angle in radians (w/o the word \"radians\"): "))
MyTan(AnAngle)

print("Compare to tan({:.4G})= {:.4g}".format(AnAngle, tan(AnAngle)))



from math import pi
Percision = 30
print("pi = {:.{}F}".format(pi, Percision))
print('{:,d} bytes in arrays saved'.format(2**30))
print("Filed {Pts} # pts in {FName}".format(Pts=10, FName='MyFilecsv'))
