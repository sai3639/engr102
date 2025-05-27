# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:47:37 2021

@author: saira

"""
def Slope(x1, y1, x2, y2):
    ComputedSlope = (y2 - y1)/ (x2 - x1)
    return ComputedSlope

def Linterpol(t0, t1, r1, t2, r2):
    return Slope(t1, r1, t2, r2) * (t2-t0) + r2



a1 = 2
b1 = 9
a2 = 11
b2 = 19

AB_Slope = Slope(a1, b1, a2, b2)

print("The slope is", AB_Slope)

print("Interpolating to get", Linterpol(7, a1, b1, a2, b2))