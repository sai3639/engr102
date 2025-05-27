# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 12:08:00 2021

@author: saira

"""


# Date:         21/9/2021
#

#Calculate how much Radon-222 is left after 5 days
#Inital amount = 3 g
# half-life = 3.8 days
inital = float(input("Please enter an inital: "))
half_life = 3.8
time = float(input("Please enter a time: "))
radon = inital*2**(-time/half_life)
print('Radon-222 left is {:.2f} g'.format(radon))
