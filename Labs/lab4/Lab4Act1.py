# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:00:02 2021

@author: saira

"""

import math
parking_time = float(input("Please enter the hours parked: "))
math.ceil(parking_time)
fees = 0


    
if parking_time > 24:
    days = parking_time/24
    parking_time = parking_time%2
    fees = days * 24


if parking_time > 0:
    fees += 4
if parking_time > 2:
    fees += 3
if parking_time > 4:
    fees += parking_time - 4
if parking_time > 21:
    fees -= parking_time - 21

 


print(fees)