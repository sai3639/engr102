# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:09:04 2021

@author: saira

"""

# Date:              29 November 2021
#finding volume of a cube with a hole in it

import numpy as np
def parta(length, width, height, radius):
    # length = int(input('enter length: '))
    # width = int(input('enter width: '))
    # height = int(input('enter height: '))
    # radius = int(input('enter radius: '))
    
    # volume_cube = length * width * height
    # volume_hole = np.pi * radius**2 * height
    # total_volume = volume_cube - volume_hole
    # return total_volume

# length = float(input('enter length: '))
# width = float(input('enter width: '))
# height = float(input('enter height: '))
# radius = float(input('enter radius: '))
    if radius < min(length/2, width/2):
        volume_cube = length * width * height
        volume_hole = np.pi * radius**2 * height
        total_volume = volume_cube - volume_hole
    elif radius >= np.sqrt((1/2)**2 + (width/2)**2):
        return 0
    
    else:
        # e = np.sqrt(radius**2 - (length/2)**2)
        # theta = np.arccos((length/2)/radius)
        # A = 1/2 * e * (length/2)
        # epi = (np.pi/2) - (2*theta)
        # B = 1/2*(radius**2) * epi
        # D = 2 * A + B
        # tot_vol = 4*D * height
        # total_volume = (length/2)**2 - tot_vol
        volume_cube = length * width * height
        theta = (np.pi/2) - (np.arccos((width/2)/radius) + np.arccos((1/2)/radius))
        quad = 4 * (theta/(2*np.pi) * np.pi*radius**2) 
        tri = (2 * np.sqrt(radius**2 - (width/2)**2) * (width/2)) + (2 * np.sqrt(radius**2 - (1/2)**2) * (1/2))
        total_volume = volume_cube - ((quad + tri) * height)
    return total_volume
