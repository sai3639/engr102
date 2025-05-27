# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 23:05:26 2021

@author: saira

"""

x1 = 2
y1 = 3
z1 = 7
x2 = 25
y2 = -5
z2 = 11

t1 = 12
t2 = 85
t0 = 45
print("At time 45 seconds:")
x0 =((x2-x1)/(t2-t1)*(t0-t1)+x1)
print("x0 =", x0, "m")
y0 = ((y2-y1)/(t2-t1)*(t0-t1)+y1)
print("y0 =", y0, "m")
z0 = ((z2-z1)/(t2-t1)*(t0-t1)+z1)
print("z0 =", z0, "m")