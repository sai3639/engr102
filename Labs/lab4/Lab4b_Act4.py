# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 22:31:48 2021

@author: saira

"""

# Date:         28 September 2021
#quadratic equation roots 

from math import sqrt 

# input coefficients 
A = float(input("Please enter the coefficient A: "))
B = float(input("Please enter the coefficient B: "))
C = float(input("Please enter the coefficient C: "))

discrim1 = (B**2 - 4 * A * C)

# find the roots 
if A != 0 and discrim1 >= 0:
    discrim = sqrt((B**2 - 4 * A * C))
    root_pos = (-B + discrim)/(2 * A)
    root_neg = (-B - discrim)/(2 * A)
elif A != 0 and discrim1 < 0:
    discrim2 = sqrt(abs(discrim1))
    #print(discrim1)
    root1 = (-B + discrim2)
    #print(root1)
    root2 = (-B + discrim2)
    root1 = str(root1)
    root2 = str(root2)
    root_pos = (root1 + " + 1.0i")
    root_neg = (root2 + " - 1.0i")
    print("The roots are x = " + root_pos + " and x = " + root_neg)
    


if A != 0 and discrim1 >= 0:
    root_pos = root_pos
    root_neg = root_neg
    if root_pos == root_neg:
        print( "The root is x =", root_pos)
    elif root_pos > root_neg:
        print("The roots are x =", root_pos, "and x =", root_neg)
        #print(root_neg)
    elif root_pos < root_neg:
        print("The roots are x =", root_neg, "and x =", root_pos)
        #print(root_pos)
elif A == 0 and B != 0:
    root_linear = -C/B
    print("The root is x =", root_linear)
elif A == B == 0 and C != 0:
    print("You entered an invalid combination of coefficients")

    
    
    

# imaginary numbers 

# coefficients = 0 
