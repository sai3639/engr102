# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 12:32:08 2021

@author: saira

"""

# Date:              11 October 2021
# print the prime numbers between 2 and 100



# for i in range(2, 101):
#     if i % num == 0:
#         print(i, "is not prime")
#     else:
#         print(i, "is prime")
        



# def is_prime(a, b):
#     for i in range(a,b):
#         for n in range (2, i):
#             if i % n ==0:
#                 print(is_prime, "is not prime")
#             else:
#                 print(is_prime, "is prime")
# is_prime(2,101)
        
# low = 2
# up = 101

# for num in range(2, 101):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 num = True
#             elif num % i != 0: # assigns num to false and stops for loop --> need to fix 
#                 num = False
#         if num == True:
#             print(num, "is not prime")
#         elif num == False:
#             print(num, "is prime")


start = 2
end = 100
prime = 0

for i in range(start, end + 1):
    if i > 1:
        for j in range(2,i):
            if (i % j == 0):
                print(i,"is not prime")
                break
        else:
            print(i, "is prime")
            prime += 1
print("\n There are", prime, "prime numbers between 2 and 100")
            




#for num in range(lower, upper):
    
