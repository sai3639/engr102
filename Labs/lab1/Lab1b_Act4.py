# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 12:41:51 2021

@author: saira
"""
print('This shows the evaluation of (e**x-1)/x evaluated close to 0')
print("My guess is 2")
from math import e
for x in range(8):
    x=1*10**-x
    print((e**x-1)/x)