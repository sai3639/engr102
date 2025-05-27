# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:39:12 2021

@author: saira

"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 18:53:11 2021

@author: cocoh



"""

#Import turtle graphics
from turtle import *

def turnRight():
    """Turns direction of drawing to the right by 90 degrees"""
    right(90)
    
def slightRight():
    """Turns direction of drawing to the right by 45 degrees"""
    right(45)
    
def turnLeft():
    """Turns direction of drawing to the left by 90 degrees"""
    left(90)
    
def slightLeft():
    """Turns direction of drawing to the left by 45 degrees"""
    left(45)
    
def headNorth():
    """If the drawing is not pointed in the north direction, it is set there"""
    if heading() != 90:
        setheading(90)
    
def headNortheast():
    """If the drawing is not pointed in the northeast direction, it is set there"""
    if heading() != 45:
        setheading(45)
    
def headNorthwest():
    """If the drawing is not pointed in the northwest direction, it is set there"""
    if heading() != 135:
        setheading(135)
    
def headEast():
    """If the drawing is not pointed in the east direction, it is set there"""
    if heading() != 0:
        setheading(0)
    
def headWest():
    """If the drawing is not pointed in the west direction, it is set there"""
    if heading() != 180:
        setheading(180)
    
def headSouth():
    """If the drawing is not pointed in the south direction, it is set there"""
    if heading() != 270:
        setheading(270)
    
def headSoutheast():
    """If the drawing is not pointed in the southeast direction, it is set there"""
    if heading() != 225:
        setheading(90) 
    
def headSouthwest():
    """If the drawing is not pointed in the southwest direction, it is set there"""
    if heading() != 315:
        setheading(315)
        
def drive(num):
    """Draws forward num amount"""
    forward(num)
    
def readFile(fileName):
    """This function opens a file, reads its contents, and returns a list of its contents"""
    instructions = open(fileName, "r")
    listInst = instructions.readlines()
    instructions.close()
    return listInst

def interpretDrive(inst):
    """This function looks for key words in the list of instructions and uses those key words to determine
    how to plot the drive"""
    for i in range(len(inst)):
        #Looks for instances of turning in the list of driving instructions, then calls a function to 
        #make the turtle graphics follow that direction
        if "Turn right" in inst[i]:
            turnRight()
        elif "Slight right" in inst[i]:
            slightRight()
        elif "Turn left" in inst[i]:
            turnLeft()
        elif "Slight left" in inst[i]:
            slightLeft()
        elif "Head northeast" in inst[i]:
            headNortheast()
        elif "Head northwest" in inst[i]:
            headNorthwest()
        elif "Head north" in inst[i]:
            headNorth()
        elif "Head west" in inst[i]:
            headWest()
        elif "Head east" in inst[i]:
            headEast()
        elif "Head southeast" in inst[i]:
            headSoutheast()
        elif "Head southwest" in inst[i]:
            headSouthwest()
        elif "Head south" in inst[i]:
            headSouth()
        #The instructions headSouth and headNorth have to be befor headNortheast/headNorthwest, etc. 
        #If they aren't, it will only see the north part first and ignore if it says east or west after it
        
        #Looks for instances of distance in the list of driving instructions, then calls a function to 
        #convert it all to the same units and then go forward that amount
        
        if ' mi' in inst[i] and not 'Pass' in inst[i] and not 'min' in inst[i]:
            num = inst[i]
            num = num.split(' ')
            number = num[0]
            number = float(number) 
            # multiply number by 10 for scale
            number = number * 10
          #  print(number)
           # number = number * 5280
            drive(number)
        elif ' mi' in inst[i] and ' min' in inst[i]:
            num = inst[i]
            num = num.split(' ')
            number = num[2]
            number = number.replace('(','')
            number = float(number)
            number = number * 10
          #  print(number)
           # number = number * 5280
            drive(number)
        elif ' ft' in inst[i] and ' s' not in inst[i]:
            num = inst[i]
            num = num.split(' ')
            number = num[0]
            number = float(number)
            number = number/5280
            number = number * 10
         #   print(number)
          #  number = number * 0.0000001644
            drive(number)
        elif ' ft' in inst[i] and ' s' in inst[i]:
            num = inst[i]
            num = num.split(' ')
            number = num[2]
            number = number.replace('(', '')
            number = float(number)
            number = number/5280
            number = number * 10
          #  print(number)
           # number = number * 0.0000001644
            drive(number)
        elif ' ft' in inst[i] and ' min' in inst[i]:
            num = inst[i]
            num=num.split(' ')
            number = num[2]
            number = number.replace('(', '')
            number = float(number)
            number = number/5280
            #number = number * 10

        
            
            
        
        
        # if "min" in inst[i]:
        #     drive()
        # elif "ft" in inst[i]:
        #     drive()
        # elif "mi" in inst[i]:
        #     drive()
            
drivingInst = readFile("Zach2PSports.txt")
interpretDrive(drivingInst)
done()
