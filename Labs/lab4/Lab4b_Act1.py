# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:51:12 2021

@author: saira

"""
# out of three numbers which is the smallest?

# Date:         28 September 2021

# input numbers
number_1 = float(input("Enter number 1: "))
number_2 = float(input("Enter number 2: "))
number_3 = float(input("Enter number 3: "))

# check which number is smallest
if number_1 > number_2 and number_2 > number_3:
    print("The smallest number is", number_3)
elif number_1 > number_2 and number_2 < number_3:
    print("The smallest number is", number_2)
elif number_1 < number_2 and number_2 < number_3:
    print("The smallest number is", number_1)
elif number_1 == number_2 == number_3:
    print("The smallest number is", number_1)
elif number_1 < number_2 and number_1 == number_3:
    print("The smallest number is", number_1)
elif number_1 > number_2 and number_2 == number_3:
    print("The smallest number is", number_2)
elif number_1 == number_2 and number_2 < number_3:
    print("The smallest number is", number_1)
