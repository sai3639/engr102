# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 11:17:32 2021

@author: saira

"""

FileID = open("Testwriting.txt", 'w')
print("When I open the file, FIleID gets assigned:", FileID)

#have to close file bc code could crash and you could lose file

if FileID:
    FileID.close()
print("When I close the file, I can NO LONGER write to it")


with open("Testwriting.txt", 'w') as FileID:  #closing file with one line
    print("FileID {} is opened:".format(FileID))
    
    
if FileID:
    print("FileID status:", FileID)
    FileID.close()
    

with open("Testwriting.txt", 'w') as FileID:  #closing file with one line
   # print("FileID {} is opened:".format(FileID))
   FileID.write("My favorite instructor is Dr. Richard\n")
   FileID.write("Dr. Richard is gread because he does not give easy A's!\n")
   
   
with open("Testwriting.txt", 'r') as File2Read:
    Line1 = File2Read.readline()
    Line2 = File2Read.readline()
    Line3 = File2Read.readline()
    
    
Line = ''
with open("Testwriting.txt", 'r') as File2Read:
    for Eachline in File2Read:
        Line += Eachline

ForLines = Line 

print("Using 'for' loop:")
print(Line)
    

Line = ''
with open("Testwriting.txt", 'r') as File2Read:
    Eachline = File2Read.readline()
    Line += Eachline
    while Eachline != '':
        Eachline = File2Read.readline()
        Line += Eachline

WhileLines = Line       
print("Using 'while' loop")
print(Line)
        


print("WhileLines == ForLines", WhileLines == ForLines)

with open("TestWriting.txt", 'r') as File2Read:
    LinesUsingRead = File2Read.read()
    print(len(LinesUsingRead))
    
print("WhileLines == LinesUsingRead?", WhileLines == LinesUsingRead)

with open("TestWriting.txt", 'r') as File2Read:
    LinesUsingReadLines = File2Read.readlines()
    print(len(LinesUsingReadLines))
    
with open("TestWriting.txt", 'r') as File2Read:
    LinesUsingList = list(File2Read)
    print(len(LinesUsingList))

print("LinesUsingList == LinesUsingRead?", LinesUsingList == LinesUsingReadLines)