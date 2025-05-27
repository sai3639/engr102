# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 21:41:49 2021

@author: saira

"""

# Date:         28 September 2021

#from math import factorial 

days = int(input("Please enter a positive value for day: "))
widgets = 0

if -1<days <=10:
   widgets = days * 10
   print("The total number of widgets produced on day", days, "is", int(widgets))
# if days > 10:
#     sum(days)
#     print(days)


elif days > 10 and days <= 50:
    n = 10*(10+1)/2
    widgets =( days*(days+1)/2) - n + 100
    print("The total number of widgets produced on day", days, "is", int(widgets))
elif days > 50 and days < 101:
    widgets = 100 + 1220 + (days - 50) * 50
    print("The total number of widgets produced on day", days, "is", int(widgets))
elif days == 101:
    widgets = 3820
    print("The total number of widgets produced on day", days, "is", int(widgets))
if days < 0:
    print("You entered an invalid number!")
    

# add days into list and sum them>
# day = [1, 2, 4]


# print(sum(day))


