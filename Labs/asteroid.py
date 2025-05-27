# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:28:06 2021

@author: saira

"""

# program checks if an input observed asteroid orbital distance
print("This program checks if an asteroid orbital distance is w/in inner planet's orbit.")



# define how close is close
rSun2Venus = 1.1e11 #m
rClose2Earth = 5e8 #m; within 5e8 of the Earth-Moon system
rSun2Earth = 1.5e11
rEarth2Moon = 4e8
rClose2Mars = rClose2Venus = 1e8 
rSun2Mars = 2.5e11
rClose2Moon = 1.5e5
rClose2ISS = 4e5
rClose2Surf = 1.25e5
r2Close2Sun = 1e9
r2Far2Care = 1e13

AsteroidDist = (float(input("Enter asteroid distance in m but just #'s w/o \"m\"): ")))

# check if w/in some margin of planet's orbit
AsteroidCloseness = "no particular large body in the solar system"
if r2Close2Sun >= AsteroidDist:
    AsteroidCloseness = "too close to the sun & will get roasted"
elif rSun2Venus - rClose2Venus <= AsteroidDist <= rSun2Venus + rClose2Venus:
    AsteroidCloseness = 'Venus'
elif rSun2Earth - rClose2Earth <= AsteroidDist <= rSun2Earth + rClose2Earth:
    AsteroidCloseness = "Earth"
    if AsteroidDist - rSun2Earth < rClose2Moon: 
        AsteroidCloseness += "'s moon"
    elif AsteroidDist - rSun2Earth < rClose2ISS:
        AsteroidCloseness += "'s space station"
    elif AsteroidDist - rSun2Earth < rClose2Surf:
        AsteroidCloseness += "'s surface"
    else:
        AsteroidCloseness += "but keep going"
elif rSun2Mars - rClose2Mars <= AsteroidDist <= rSun2Mars + rClose2Mars:
    AteroidCloseness = "Mars"
elif r2Far2Care > AsteroidDist > rSun2Mars + rClose2Mars:
    AsteroidCloseness = "to making a little bright dot in Jupiter's atmosphere"
else: 
    AsteroidCloseness = "the edge of the solar system & of no threat"



# print to which planet it is close
print("The asteroid is near", AsteroidCloseness)






