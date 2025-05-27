# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 12:42:02 2021

@author: saira

"""


# Date:        21/9/2021
#

from math import pi, sqrt, sin, tan

#calculating dimensions of shapes given area 
area = float(input("Please enter the area: "))

def circle(A):
    radius = sqrt(area/(pi)) 
    #radius = str(radius)
    #print("A cricle with area", area," has a radius {.:3f}".format(radius))
   # print(area)
    print("A circle with area {:.2f}".format(area), "has a radius {:.3f}".format(radius))



def triangle(A1):
    #area = 1/2 *side * cos(60)
    #print(area)
    #side = sqrt((2 *area)/sin(60))
    side = (2/3)*3**(3/4)*sqrt(area)
    print("An equilateral triangle with area {:.2f}".format(area),"has a side {:.3f}".format(side))


def square(A2):
    #print(area)
    side_square = sqrt(area)
    print("A square with area {:.2f}".format(area),"has a side {:.3f}".format(side_square))

def pentagon(A3):
    #print(area)
    #side_pent = ((sqrt(area)/((5*((sqrt(20)+5)**(1/4))))))*(25**(3/4))
    side_pent = sqrt((4*area*tan(pi/5))/(5))
    print("A pentagon with area {:.2f}".format(area),"has a side {:.3f}".format(side_pent))


def dodecagon(A4):
    side_dod = sqrt((4*area*tan(pi/12))/(12))
    print("A dodecagon with area {:.2f}".format(area), "has a side {:.3f}".format(side_dod))

def main(area):
    area = circle(area)
    area = triangle(area)
    area = square(area)
    area = pentagon(area)
    area = dodecagon(area)

area = main(area)
    
