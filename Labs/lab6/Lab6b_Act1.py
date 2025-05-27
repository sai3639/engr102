# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 22:41:52 2021

@author: saira

"""

# Date: 13 October2021
# Collatz Sequence





def collatz(n):
    iterations = 0
    while n != 1:
        print(n, end=', ')
        if (n % 2):
            # n is odd
            n = 3*n + 1
        else:
            # n is even
            n = n//2
        iterations += 1
    print(1, end='')
    print("\nIt took", iterations, "iterations to reach 1")
 
 
n = int(input('Enter a positive integer to compute the Collatz sequence: '))
startcol = n
startcol = str(startcol)
#iterations = 0
print('Here is the Collatz sequence starting at '+startcol+':', end='\n')

collatz(n)
#iterations = 0
