# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 12:29:30 2021

@author: saira

"""
from math import pi
digits = int(input("Please enter the number of digits of precision for pi: "))
#print(digits)
print("The value of pi to", digits, "digits is: {:.{}f}".format(pi, digits))