# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 12:04:31 2021

@author: saira

"""


# Date:         21/9/2021
#

#Calculate wavlength of x-rays with a distance of 0.025 nm and an anle of 25 degrees
from math import sin, radians
distance = float(input("Pelase enter the distance: "))
degree = float(input("Please enter the degree: "))
wavelength = 2*(distance)*sin(radians(degree))
print('Wavelength is {:.4f}'.format(wavelength), "nm")

