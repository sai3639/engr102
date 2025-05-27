# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 12:33:02 2021

@author: saira

"""


# Date:         21/9/2021
#

#Calculate the pressure of 5 moles of an ideal gas 
#With a volume of 0.15 m^3 
#And temperature of 425 K
#divide by 1000 to go from Pascals to kilopascals?
print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles: "))
volume = float(input("Please enter the volume (m^3): "))
temp = float(input("Please enter the temperature (K): "))
gas_constant = 8.314
pressure = (temp*gas_constant*moles)/(volume*1000)
print('Pressure is {:.0f} kPa'.format(pressure)) 
