# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 11:17:16 2021

@author: saira

"""


# Date:         23 September 2021

import math
parking_time = float(input("Enter # of hours parked: "))
math.ceil(parking_time)


fees = 4 


if 0< parking_time <=2:
    print(fees)
elif 2<parking_time<=4:
    fees = fees + 3
elif 4<parking_time:
    fees = fees + parking_time
print(fees)   
if parking_time > 24:
    days = parking_time/24
    fees3 = (days*24) + fees
    print(fees)
if parking_time < 0:
    fees = fees + 36
    print(fees)
