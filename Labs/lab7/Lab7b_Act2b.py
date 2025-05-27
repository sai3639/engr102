# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 12:42:56 2021

@author: saira

"""

# Date:              22 October 2021
#

hourly_temperature = input("Enter three or more values separated by spaces: ")
hourly_temperature = hourly_temperature.split()
# enter seperator 
separator = input("Enter a two-character separator: ")
for temp in hourly_temperature:
    if temp != hourly_temperature[len(hourly_temperature)-1]:
        print(temp,'', end=separator + ' ')
    else:
        print(temp, end=' \n')

# print hourly temperature 
# align <>
