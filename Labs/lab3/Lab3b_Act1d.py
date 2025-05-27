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
moles = float(input("Please enter moles: "))
volume = float(input("Please enter volume: "))
temp = float(input("Please enter temperature: "))
gas_constant = 8.314
pressure = (temp*gas_constant*moles)/(volume*1000)
print('Pressure is {:.0f} kPa'.format(pressure)) 
