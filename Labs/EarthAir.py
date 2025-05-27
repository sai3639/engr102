# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 12:38:09 2021

@author: saira

"""

import numpy as np
import matplotlib.pyplot as plt


def EarthT(Alt):
    # T(h) = T_SL - k * h, for T< 20000 m
    # T(h) = Const. @ h >= 20 km
    T_SL = 22 # C
    Coef = (-20 - T_SL)/2e4
    TLowerAtm = T_SL + Coef * Alt[np.where(Alt < 2e4)]
    TUpperAtm = -20 + 0 * Alt[np.where(Alt  >= 2e4)]
    
    
    return np.append(TLowerAtm, TUpperAtm)


Altitude = np.linspace(0, 4e4, 50)
TEarthAtm = EarthT(Altitude)


plt.figure()
plt.plot(TEarthAtm, Altitude, color = 'red')
plt.title("Earth's isotherms @ altitude")
plt.xlabel("Temperature, $^o C$")
plt.ylabel("Altitdue, m")

plt.show()
