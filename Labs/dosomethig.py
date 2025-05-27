# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 11:41:09 2021

@author: saira

"""

def doSomethingElse(a,b):
    a+= b
    b = 7
    return a,b


x = 1
y = 2
x,y = doSomethingElse(x, y)
print(x)
print(y)



def doList(a):
    a = [10,11,12]
    
x = [1,2,3]
doList(x)
print(x)


def doConcList(a):
    a+= [10,11,12]

x = [1,2,3]
doConcList(x)
print(x)



import numpy as np

def doListNArray(a):
    a += np.array([10,11,12])
    
x = [1,2,3]
doListNArray(x)
print(x)


def doArrayNList(a):
    a+= [10,11,12]
    
x = np.array([1,2,3])
doArrayNList(x)
print(x)



myList = [1,23]
myList2 = myList[:]
myList[0] = 24
print(myList, myList2)



myList = [1,23]
myList2 = myList
myList[0] = 24
print(myList, myList2)



mystr = 'Howdy'
mylist = [1,2,3]
mytuple = (mystr, mylist)
print(mylist,mytuple)


mystr = 'Hi'
mylist[0] = 5
print(mylist,mytuple)

