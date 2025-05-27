# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 12:05:24 2021

@author: saira

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 *np.pi, 100)     # 100 = # of points you want in the plot
                                      # linspace makes sure points are evenly spaced and includes and 2pi

yCos = np.cos(x[np.where(x<np.pi)])   # gets index of where x is less than pi
ySin = np.sin(x[np.where(x>=np.pi)])

y = np.append(yCos, ySin)

plt.figure()
plt.plot(x, y, "--b")

