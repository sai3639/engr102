# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 16:15:57 2021

@author: saira

"""

filename = input('filename: ')


# read file

with open(filename, 'r') as directions:
    list1 = []
    list2 = []
    for line in directions:
        if line != '\n':
            list2.append(line)
            if len(list2) == 2 or len(list2) == 3:
                list1.append(list2)
        else:
            list2 = []
    print(list1)

   # print(list1)
