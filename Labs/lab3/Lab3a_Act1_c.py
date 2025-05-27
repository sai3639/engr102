# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:05:27 2021

@author: saira

"""

# Date:         20 September 2021

#atmospheres to milimeters of mercury
atmospheres = float(input("Please enter the number of atmospheres to be converted to millimeters of mercury: "))
millimeters_mercury = atmospheres*760
print("{:.2f}".format(atmospheres), "atmospheres is equivalent to {:.2f}".format(millimeters_mercury), "millimeters of mercury")
