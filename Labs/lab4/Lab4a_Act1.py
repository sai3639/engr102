# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:26:23 2021

@author: saira

"""

# Date:         23 September 2021

import math
print("Enter the hours parked as a decimal number. Include a negative sign if the ticket is lost.")
parking_time = float(input("Please enter the hours parked: "))
hours = parking_time
if parking_time < 0:
    parking_time = math.floor(parking_time)
elif parking_time > 0:
    parking_time = math.ceil(parking_time)
fees = 0

if parking_time < 0:
    parking_time = parking_time * -1 
    fees+=36
if parking_time > 24:
    #parking_time %= 24
    days = parking_time/24
    days = round(days)
    #parking_time = parking_time - fees
    #print(parking_time)
    fees1 = days *24
    fees += days *24
    parking_time = parking_time - fees1
    #parking_time = abs(parking_time)
    #print(fees1)
    #fees = days *24
   # fees += 24
    #print(fees)
    # days = parking_time/24
    # parking_time = parking_time%2
    # fees += days * 24
    #print(fees)
   
if parking_time > 0:
    fees += 4
if parking_time > 2:
    fees += 3
if parking_time > 4:
    #print(parking_time)
    fees += parking_time - 4
if parking_time > 21:
    fees -= parking_time - 21



print("Parking for", hours, "hours please pay $" + str(int(fees)))
