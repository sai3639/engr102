# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:11:58 2021

@author: saira

"""

# Date:         20 September 2021

#watts to BTU per hour
watts = float(input("Please enter the number of watts to be converted to BTU per hour: "))
BTU = watts * 3.412141633
print("{:.2f}".format(watts), "watts is equivalent to {:.2f}".format(BTU), "BTU per hour")
