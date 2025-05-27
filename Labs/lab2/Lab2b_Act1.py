# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 14:14:15 2021

@author: saira
"""

# Date:         8/9/2021
#
#Calculate the force in Newtons applied to an object with a mass of 2kg and acceleration of 5m/s^2
mass = 2
acceleration = 5
force = mass * acceleration 
print("Force is", force, "N")


#Calculate wavlength of x-rays with a distance of 0.025 nm and an anle of 25 degrees
from math import sin, radians
distance = 0.025
degree = 25
wavelength = 2*(distance)*sin(radians(degree))
print('Wavelength is', wavelength, 'nm')

#Calculate how much Radon-222 is left after 5 days
#Inital amount = 3 g
# half-life = 3.8 days
inital = 3
half_life = 3.8
time = 5
radon = inital*2**(-time/half_life)
print('Radon-222 left is', radon, 'g')


#Calculate the pressure of 5 moles of an ideal gas 
#With a volume of 0.15 m^3 
#And temperature of 425 K
#divide by 1000 to go from Pascals to kilopascals?
moles = 5
volume = 0.15
temp = 425
gas_constant = 8.314
pressure = (temp*gas_constant*moles)/(volume*1000)
print('Pressure is', pressure, 'kPa') 
