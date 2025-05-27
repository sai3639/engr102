# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:18:17 2021

@author: saira

"""

# Date:         20 September 2021

#celsius to degree rankine 
celsius = float(input("Please enter the number of degrees Celsius to be converted to degrees Rankine: "))
rankine = (celsius * (9/5)) + 491.67
print("{:.2f}".format(celsius), "degrees Celsius is equivalent to {:.2f}".format(rankine), "degrees Rankine")
