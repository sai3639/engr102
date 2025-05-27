# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 11:18:05 2021

@author: saira

"""

#BooLying.py plays w/bool

CompNumbers = ((3>5) and (5>4))

print('CompNumbers =', CompNumbers)

TFreeze = 0
TVapor = 100
TPlasma = 1e6

Temp = input("How hot is it(in C, but w/o the \"C\")?")
if Temp.isalpha():
    print("You did not enter a # but", Temp)
elif not Temp.isdecimal():
    print('You did not enter a decimal # but', Temp)
elif not Temp.isdigit():
    print("No #'s in you're input:", Temp)
else:
    print(Temp, end=' ')
    Temp = float(Temp)
    print('converts to', Temp)

def isSolid(T): 
    return TFreeze > Temp


def isALiquid(T):
    if isinstance(T, float) or isinstance(T, int):
        return TFreeze < T < TVapor 
    else:
        return 'You did not enter a valid #!'


isLiquid = (Temp >= 0) and (Temp <= 100)
isVapor = Temp > TVapor 
isPlasma = 1e9 > TPlasma < Temp

if isSolid(Temp):
    print(isSolid(Temp), "= is solid because {:.2f} > {:.2f}".
          format(TFreeze, Temp))
elif isLiquid:
    print(isLiquid, "= isLiquid because {:.2f} < {:.2f} < {:.2f}".
          format(TFreeze, Temp, TVapor))
    if 0 < Temp < 20:
        print("& the water @ {:.2f} is cold!".format(Temp))
    elif 20 <= Temp <= 30:
        print("& the water @ {:.2f} is room temp.!".format(Temp))
    elif 30 < Temp < 100:
        print("& the water @ {:.2f} is hot!".format(Temp))
    else:
        print("Don't drink this water!")
elif isVapor:
    print(isVapor, "that is vapor because {:.2f} > {:.2f}".
          format(Temp, TVapor))
else: 
    print("You found a new state of matter!")


