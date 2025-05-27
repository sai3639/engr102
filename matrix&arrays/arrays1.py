# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:47:42 2021

@author: saira

"""

# Date:         17 November  2021

#arrays

import numpy as np
#import mathplotlib as plt

# make the arrays bud
A = np.arange(12).reshape(3,4)
B = np.arange(8).reshape(4,2)
C = np.arange(6).reshape(2,3)


# A = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
# B = np.array([[0,1], [2,3], [4,5], [6,7]])
# C = np.array([[0, 1, 2], [3, 4, 5]])


print('A = ',A, '\n')
print('B = ',B, '\n')
print('C = ',C, '\n')

# D = ABC

#B.resize(A.shape)
#C.resize(A.shape)
#D = A  * B * C
D = A.dot(B)
D = D.dot(C)
print('D = ',D, '\n')



# transpose D
d_transpose = D.T

print('D^T = ',d_transpose, '\n')


E = np.sqrt(D)/2
print('E = ',E)





