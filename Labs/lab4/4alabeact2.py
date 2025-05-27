# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:07:33 2021

@author: saira

"""

A = int((input("Please enter the coefficient A: ")))
B = int((input("Please enter the coefficient B: ")))
C = int((input("Please enter the coefficient C: ")))

if A == -1:
    A = '-'
elif A == 0:
    A = ()
elif A > 0:
    A = A
if B > 0:
    
    


quad = "{:1d}x^2 {:1d}x {1:d}".format(A, B, C)
print(quad)