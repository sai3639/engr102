# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 12:45:14 2021

@author: saira

"""

#quadratic 
# Date:         23 September 2021



A = int((input("Please enter the coefficient A: ")))
B = int((input("Please enter the coefficient B: ")))
C = int((input("Please enter the coefficient C: ")))


# if B == 0:
#     B = ""
# if C == 0:
#     C = ""


#if A == 0:
 #   A = "\b"
    #x = "\b"
if A == -1:
    A = "- " + "x^2"
elif A == 1:
    A = "x^2"
elif A < 0:
    A = A * -1
    A = "-" + str(A) + "x^2"
elif A > 0:
    A = str(A) + "x^2"

# if B == 0:
#     B = "\b"
if B < 0:
    B = B * -1
    B = "- " + str(B) + "x"
elif B == 1:
    B = '+ x'
elif B > 0 and A == 0:
    B = str(B) + "x"
elif B > 0:
    B = "+ " + str(B) + "x"

# if C == 0:
#     C = "\b"
if C < 0:
    C = C * -1
    C = "- " + str(C)
elif C > 0:
    C = "+ " + str(C)

if A ==0:
    quad = ("{:1s} {:1s}".format(B,C) + " = 0") 
elif B == 0:
    quad = ("{:1s} {:1s}".format(A,C) + " = 0")
elif C == 0:
    quad = ("{:1s} {:1s}".format(A,B) + " = 0")
else:
     quad = ("{:1s} {:1s} {:1s}" . format(A, B, C) +" = 0")

print("The quadratic equation is", quad)
