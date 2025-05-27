# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 12:49:27 2021

@author: saira

"""

# Date:              22 October 2021
#dot product, magnitude of two vectors

from math import sqrt 

A = input("Enter the elements for vector A: ")
B = input("Enter the elements for vector B: ")

A = A.split(' ')
B = B.split(' ')
number = 0
dot_product = 0
A_plus_B = []
A_minus_B = []
magnitude_A = 0
magnitude_B = 0
#A[0] = float(A[0])
#A[1] = float(A[1])
#A[2] = float(A[2])
#B[0] = float(B[0])
#B[1] = float(B[1])
#B[2] = float(B[2])
#magnitude_A = sqrt((A[0]**2 + (A[1])**2 + (A[2])**2))
#print("The magnitude of vector A is {:.4f}".format(magnitude_A))
#magnitude_B = sqrt((B[0])**2 + (B[1])**2 + (B[2])**2)
#print("The magnitude of vector B is {:.4f}".format(magnitude_B))

for number in range(len(A)) and range(len(B)): 
    number = int(number)
    dot_product += float(A[number])*float(B[number])
    magnitude_A += ((float(A[number])**2))
    magnitude_B += ((float(B[number])**2))

    #print(A)
    #print(B)
    #print(A[number])
    #print(B[number])
    plus = float(A[number]) + float(B[number])
    minus = float(A[number]) - float(B[number])
    #plus = float(plus)
    #minus = float(minus)
    A_plus_B.append(plus)
    A_minus_B.append(minus)
    #magnitude_A = sqrt()
    #print(plus)
    #plus = int(A[0]) + int(B[0])
    #print(plus)
    
    number += 1
    #print(plus)
    # plus = A[number] + B[number]
    # minus = A[number] - B[number]
    # print(plus)
#     # print(minus)
# A[0] = float(A[0])
# A[1] = float(A[1])
# A[2] = float(A[2])
# B[0] = float(B[0])
# B[1] = float(B[1])
# B[2] = float(B[2])
magnitude_A = sqrt(magnitude_A)
magnitude_B = sqrt(magnitude_B)
#magnitude_A = sqrt((A[0]**2 + (A[1])**2 + (A[2])**2))
print("The magnitude of vector A is {:.4f}".format(magnitude_A))
#magnitude_B = sqrt((B[0])**2 + (B[1])**2 + (B[2])**2)
print("The magnitude of vector B is {:.4f}".format(magnitude_B))
print("A + B is", A_plus_B)
print("A - B is", A_minus_B)

print("The dot product is", dot_product)
