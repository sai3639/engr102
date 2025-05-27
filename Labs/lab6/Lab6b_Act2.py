# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 23:35:47 2021

@author: saira

"""


# Date:             13 October2021
#




# inputs
integer = int(input("Enter an integer: "))

total = 0


for number in range(integer + 1):
    total = number + total
print("The sum of all integers from 0 to", integer, "is", total)


product = 1
for i in range(1, integer + 1):
    product = product * i 
print("The product of all integers from 1 to", integer, "is", product)
