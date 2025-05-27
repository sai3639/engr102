# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:15:31 2021

@author: saira

"""

# Date:         20 September 2021

#liters to gallons

liters = float(input("Please enter the number of liters per second to be converted to gallons per minute: "))
gallons = liters * 15.8503
print("{:.2f}".format(liters), "liters per second is equivalent to {:.2f}".format(gallons), "gallons per minute")
