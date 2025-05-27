# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 20:52:19 2021

@author: saira

"""

# Date:         28 September 2021

########### Part A ##########
# roundoff is different

a = 1 / 7
print('a =', a)
b = a * 7
print('b = a * 7 =', b)

# b = 1.0 

c = 2 * a
d = 5 * a
f = c + d
print('f = 2 * a + 5 * a =', f)

# b = 0.99999 - no roundoff 

from math import sqrt
x = sqrt(1 / 3)
print('x =', x)
y = x * x * 3
print('y = x * x * 3 =', y)
z = x * 3 * x
print("z = x * 3 * x =", z)

# no roundoff - 0.9999


########### Part B ##########

TOL = 1e-10
# check if b and f are equal within specified tolerance
if abs(b-f) < TOL:
    print('b and f are equal within tolerance of', TOL)
else:
    print('b and f are NOT equal within tolerance of', TOL)

TOL1 = 1e-10
# check if y and z are equal within specified tolerance
if abs(y-z) < TOL1:
    print('y and z are equal within tolerance of', TOL)
else:
    print('y and z are NOT qual within tolerance of', TOL)


########### Part C ##########

m = 0.1
print('m =', m)
n = 3 * m
print('n = 3 * m = 0.3', n == 0.3)
p = 7 * m
print('p = 7 * m = 0.7', p == 0.7)
q = n + p
print('q = 1', q == 1)
