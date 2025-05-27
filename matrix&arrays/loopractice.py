# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:15:04 2021

@author: saira

"""

# make matrix

# 1 0 0 0
# 0 1 0 0
# 0 0 1 0 
# 0 0 0 1


nRows = input("# rows: ")
nCols = input("# columns: ")

if nRows.isdigit() and nCols.isnumeric():
    nRows = int(nRows)
    nCols = int(nCols)
    
    for EachRow in range(nRows):
        for EachCol in range(nCols):
            if EachRow == EachCol:
                print("{:^3d}".format(1), end='') # carrot means center it  
            else:
                print("{:^3d}".format(0), end='')
        print()
        
    matrix = []
    for EachRow in range(nRows):
        EachRowMatrix = []
        for EachCol in range(nCols):
            if EachRow == EachCol:
                EachRowMatrix.append(1)
            else:
                EachRowMatrix.append(0)
        matrix.append(EachRowMatrix)
    print(matrix)
            
                
else:
    print("Either", nRows, "or", nCols, "failed input criteria!")
    

            
            
