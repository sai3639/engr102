# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 11:16:05 2021

@author: saira

"""

RowsNColumns = input("type in total rows and columns seperated by ',': ")

RowsCols = RowsNColumns.split(',')


Rows = int(RowsCols[0])
Cols = int(RowsCols[1])


TriDiagMat = []
for EachRow in range(Rows):
    ThisRow = []
    for EachCol in range(Cols):
        if EachCol - 1 <= EachRow <= EachCol + 1:
            ThisRow += [ - 1 ]
        else:
            ThisRow += [  0 ]    
    TriDiagMat += [ThisRow]

    
#print(TriDiagMat)

for EachRow in range(Rows):
    for EachCol in range(Cols):
        print("{:^3d}".format(TriDiagMat[EachRow][EachCol]), end='')
    print()

    

# rows alternate sign
AltMat = []
for EachRow in range(Rows):
    ThisRow = []
    for EachCol in range(Cols):
        if EachRow % 2:
            ThisRow += [-1]
        else:
            ThisRow += [0]
    AltMat += [ThisRow]

print(AltMat)
#int(AltMat)        
for EachRow in range(Rows):
    for EachCol in range(Cols):
        print("{:^3d}".format(AltMat[EachRow][EachCol]), end='')
    print()
