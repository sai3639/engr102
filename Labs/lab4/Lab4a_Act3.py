# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:34:23 2021

@author: saira

"""


# Date:         23 September 2021


########### Part A ###########


a = input("Enter True or False for a: ")
b = input("Enter True or False for b: ")
c = input("Enter True or False for c: ")

# a true or false
if a == "True":
    a = True
elif a =="T":
    a = True
elif a == "t":
    a = True 
if a == "False":
    a = False
elif a == "F":
    a = False
elif a =="f":
    a = False

# b true or false
if b == "True":
    b = True
elif b =="T":
    b = True
elif b == "t":
    b = True 
if b == "False":
    b = False
elif b == "F":
    b = False
elif b =="f":
    b = False
    
    
# c true or false
if c == "True":
    c = True
elif c =="T":
    c = True
elif c == "t":
    c = True 
if c == "False":
    c = False
elif c == "F":
    c = False
elif c =="f":
    c = False


########### Part B ###########
#print(bool(a))
d = a and b and c 
f = a or b or c
print("a and b and c:", d) 
print("a or b or c:", f)


########### Part C ###########


if a and not b or not a and b == True:
    XOR = True 
elif a and b == True:
    XOR = False 
elif a or b and b or a == False:
    XOR = False 
print("XOR:", XOR)

if a and b and c == True:
    oddnumber = True
elif (a and b and not c) or (a and not b and c) or (not a and b and c) == True:
    oddnumber = False
elif (a and not b and not c) or (not a and b and not c) or (not a and not b and c) == True:
    oddnumber = True
elif (a and b and c) or (a and b and not c) or (a and not b and c) or (not a and b and c) == False:
    oddnumber = False

print("Odd number:", oddnumber)


########### Part D ###########
#(not(a and not b) or (not c and b) and (not b) or (not a and b and not c) or (a and not b))
Complex1 = (-(a + (-b)) * ((-c) + b)) + ((-b)*(-a + b + (-c)) * (a + (-b)))
Complex2 = (-((b * -c) + (-a * -c))) * (-(c * -(b +c))) * (a + -c) + (-a *(a +b +c) * (a +((b + -c) * (-b))))
simple1 = (-a + b) * (-c + b) + (a*b - b**2 + c*b) * (a + -b)
simple2 = (-b * c) + (a * c) * -c + (b + c) * (a + -c) + (-a**2 - a *b - a *c) * ( - a * b**2 + a * b * c)

Complex1 = bool(Complex1)
Complex2 = bool(Complex2)
simple1 = bool(simple1)
simple2 = bool(simple2)
print("Complex 1:", Complex1)
print("Complex 2:", Complex2)
print("Simple 1:", simple1)
print("Simple 2:", simple2)
