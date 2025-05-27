# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:16:35 2021

@author: saira

"""
#interpolation
# Date:         20 September 2021

def interpolate(x1,x2,y1,y2,z1,z2,t1,t2,t0):
    x = (x1+(x2-x1)/(t2-t1)*(t0-t1))
    y = (y1+(y2-y1)/(t2-t1)*(t0-t1))
    z = (z1+(z2-z1)/(t2-t1)*(t0-t1))
    print("At time {:1.1f}".format(t0), "seconds the object is at ({:1.2f}, {:1.2f}, {:1.2f})".format(x,y,z))
    #return x, y, z

t1 = float((input("Enter time 1: ")))
x1 = float(input("Enter the x position of the object at time 1: "))
y1 = float(input("Enter the y position of the object at time 1: "))
z1 = float(input("Enter the z position of the object at time 1: "))

t2 = float(input("Enter time 2: "))
x2 = float(input("Enter the x position of the object at time 2: "))
y2 = float(input("Enter the y position of the object at time 2: "))
z2 = float(input("Enter the z position of the object at time 2: "))

mid = (t2-t1)/(5-1)
t0 = t1


print()
interpolate (x1, x2, y1, y2, z1, z2, t1, t2, t0)
t0+=mid

interpolate(x1, x2, y1, y2, z1, z2, t1, t2, t0)
t0+=mid


interpolate(x1, x2, y1, y2, z1, z2, t1, t2, t0)
t0+=mid


interpolate(x1,x2, y1, y2, z1, z2, t1, t2, t0)
t0+=mid
 
interpolate(x1, x2, y1, y2, z1, z2, t1, t2, t0)
t0+=mid


    
