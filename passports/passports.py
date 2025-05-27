# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 16:55:38 2021

@author: saira

"""

# Date:         8 NOvember 2021
#valid passports
# read through a file with passports
# check to see if certain specifics are in that passport
# write a new file containing only valid passports


    
passport = open('Lab9a_input.txt', 'r')
pass_read = passport.read()
pass_split = pass_read.split('\n\n')


valid_pass = 0

valid_passport = open('Lab9a_Act1a_valid.txt', 'w')


for x in pass_split:
    
    if 'byr' and 'iyr' and 'eyr' and 'hgt' and 'hcl' and 'ecl' and 'pid' in x:
        valid_pass += 1
        valid_passport.write(x)
        valid_passport.write('\n\n')
    
    # if 'byr' in x:
    #     if 'iyr' in x:
    #         if 'eyr' in x:
    #             if 'hgt' in x:
    #                 if 'hcl' in x:
    #                     if 'ecl' in x:
    #                         if 'pid' in x:
    #                             valid_pass +=1
    #                             valid_passport.write(x)
    #                             valid_passport.write('\n\n')
print("There are", valid_pass, 'valid passports')

passport.close()
valid_passport.close()
