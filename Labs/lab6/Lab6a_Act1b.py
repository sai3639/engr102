# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 12:10:12 2021

@author: saira

"""

# Date:11 October 2021
#


# a = a1 + (n-1)d

# a1 = 1st block?

# areatop = 0
# areaside = 0

# areatop = ((length * (i + 1))**2) - ((length * (i))**2)
# areaside = ((length * (i + 1)) * length )* 4
# area += areatop + areaside


length = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))

if 0 < length < 1 or 1 < length < 2:
    area = layers/2*(2*(5*length**2) + (layers-1)*(length**2*6))
    print("You need {:.2f}".format(area), "square meters of gold foil to cover the pyramid")
else:
    a1 = 5*(length)**2
    area = layers/2*(2*a1 + (layers - 1)*6)
    print("You need {:.2f}".format(area), "square meters of gold foil to cover the pyramid")
