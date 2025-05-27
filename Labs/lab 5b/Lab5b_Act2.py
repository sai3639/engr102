# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:27:28 2021

@author: saira

"""


# Date:         7 October 2021
#




# input
strain = float(input("Enter the strain: "))

# variables based on sections of graph
young_mod = 4300
plastic = 10
strain_hard = 137.5
necking = -100

# strain  in between 0.01 and 0.06

if 0.01 <= strain <= 0.06:
    stress = plastic*(strain-0.01)+43
    print("The stress is approximately {:.1f}".format(stress))
# stress in between 0.06 and 0.18
elif 0.06 < strain <= 0.18:
    stress = strain_hard*(strain-0.06) + 43.5
    print("The stress is approximately {:.1f}".format(stress))
# stress in between 0.18 and 0.27
elif 0.18 < strain <= 0.27:
    stress = necking *(strain-0.18) + 60
    print("The stress is approximately {:.1f}".format(stress))
elif 0 <= strain< 0.01:
    stress = (young_mod)*(strain-0) + 0
    print("The stress is approximately {:.1f}".format(stress))
elif strain < 0:
    print("Strain is undefined in that region")
elif strain > 0.27:
    print("The strain is fractured!")




    






