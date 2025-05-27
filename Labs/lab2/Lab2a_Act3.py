# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:08:53 2021

@author: saira

"""


# Date:         13 September 2021

#Lab 2a_Act 3 part 1

#Lab2a_Act3
time_1 = 10
time_2 = 55
time_0 = 25
position_1 = 2025
position_2 = 23025 

iss_final = ((position_2 - position_1)/(time_2 - time_1)) * (time_0-time_1) + position_1
print("Part 1:")
print("For t = 25 minutes, the position p =",iss_final,"kilometers")


#Lab_2a_Act3 part 2 
from math import pi 
radius = 6745
circumference = 2*pi*radius
time_0 = 300 
iss_final = ((position_2 - position_1)/(time_2 - time_1)) * (time_0-time_1) + position_1
remainder = iss_final%circumference 
print("Part 2:")
print("For t = 5.0 hours, the position p =",remainder,"kilometers")

