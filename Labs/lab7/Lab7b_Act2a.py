# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 12:32:51 2021

@author: saira

"""

# Date:              22 October 2021
#


prices = input("Enter three or more prices separated by spaces: ")

prices = prices.split(' ')

#money = []

#for x in prices 

for dollar in prices:
    #prices = float(prices)
    #dollar = float(dollar)
    #money.append(prices)
   # print("$ "  + dollar)
    print("${0:>7s}".format(dollar))
    #print({:})
    #dollar = [len(s.split('.',1)[0]) for s in prices]
    #print(dollar)
