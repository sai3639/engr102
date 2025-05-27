# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 11:36:59 2021

@author: saira
"""

# Date:         2/9/2021
#
#Calculate the force in Newtons applied to an object with a mass of 2kg and acceleration of 5m/s^2
print('Force is', 2*5, 'N')


#Calculate wavlength of x-rays with a distance of 0.025 nm and an anle of 25 degrees
from math import sin, radians
print('Wavelength is', 2*(0.025)*sin(radians(25)), 'nm')

#Calculate how much Radon-222 is left after 5 days
#Inital amount = 3 g
# half-life = 3.8 days
print('Radon-222 left is', 3*2**(-5/3.8), 'g')


#Calculate the pressure of 5 moles of an ideal gas 
#With a volume of 0.15 m^3 
#And temperature of 425 K
#divide by 1000 to go from Pascals to kilopascals?
print('Pressure is', (425*8.314*5)/(0.15*1000), 'kPa') 
