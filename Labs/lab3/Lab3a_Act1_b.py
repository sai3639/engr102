# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:00:01 2021

@author: saira

"""

# Date:         20 September 2021
#kilometers to miles
#import math
kilometers = float(input("Please enter the number of kilometers to be converted to miles: "))
miles = kilometers*0.62137
#math.floor(miles)
print("{:.2f}".format(kilometers), "kilometers is equivalent to {:.2f}".format((miles)), "miles")
