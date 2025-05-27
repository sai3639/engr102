# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:27:48 2021

@author: saira

"""

# Date: 11 October 2021
#how to calculate the area of a pyramid made out of cubes with gold foil
#only covering the square faces you can see 




length = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))


area = 0 
areatop= 0 
areaside = 0

for i in range(layers):
    areatop = ((length * (i + 1))**2) - ((length * (i))**2)
    areaside = ((length * (i + 1)) * length )* 4
    area += areatop + areaside

print("You need {:.2f}".format(area), "square meters of gold foil to cover the pyramid")






# surface area of one cube given side_length

# number of cubes in each layer = layer**2
# number of cubes you can't see in second layer = 1
# number of cubes you can't see in thrid layer = 4
# number of cubes you can't see in fourth layer = 9
# number of cubes you can't see in fifth layer = 16
# number of cubes you can't see in 6th layer = 25
# # of cubes you can't see in a given layer = (previous layer **2)
    # # of cubes in a given layer = (layers**2) - (layers - 1)**2


# surface area of cube - side you can't see 
# surface area - (one face) * the number of cubes in that layer?
# i + 1 + 2i
# side length * 4
#for i in range(layers):

    
# corner block = 3 faces showing (except 1st layer)
# rest of blocks = 2 faces showing
# # of blocks in layer - 4 = number of blocks that are not corner 


# area_side = 4(length(i + 1))
    
# area_side = 0

# for i in range(layers):
#     area_side = 4(length(i+1))
    #cubes = (layers**2) - (layers-1)**2
    
    
# length(i +1) *4
