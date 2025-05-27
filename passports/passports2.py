# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 20:23:55 2021

@author: saira

"""

# Date:         8 November  2021
#passports #2


passport = open('Lab9a_input.txt', 'r')

pass_read = passport.read()
pass_split = pass_read.split('\n\n')


valid_pass = 0

valid_passport = open("Lab9a_Act1b_valid.txt", 'w')

passport.close()

Passport = []
valid_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for x in pass_split:
    pass_dict = {}
    invalid = 0
    for keys in valid_keys:
        if keys not in x:
            invalid = 1
    if invalid == 1:
        continue
    stuff = x.split()
    for s in stuff:
        name = s.split(':')
        pass_dict[name[0]] = name[1]
    pass1 = 0
    if 1920<=int(pass_dict['byr']) <= 2005: # checking if birth year is valid
        pass1 += 1
    if 2011 <= int(pass_dict['iyr']) <= 2021:
        pass1 += 1
    if 2021 <= int(pass_dict['eyr']) <= 2031:
        pass1 += 1
    if 'cm' in pass_dict['hgt']:
        if 150 <= int(pass_dict['hgt'][:-2]) <= 193:
            pass1 += 1
    if 'in' in pass_dict['hgt']:
        if 59 <= int(pass_dict['hgt'][:-2]) <= 76:
            pass1 += 1
    if pass_dict['hcl'][0] == '#' and len(pass_dict['hcl']) ==7:
        t = True
        for char in pass_dict['hcl']:
            if char not in '#0123456789abcdef':
                t = False
                break
        if t:
            pass1 += 1
    if pass_dict['ecl'] in 'amb blu brn gry grn hzl oth':
        pass1+= 1
    if len(pass_dict['pid']) ==9:
        pass1 += 1
    if pass1 ==7:
        valid_passport.write(x + '\n\n')
        valid_pass += 1
print("There are", valid_pass, 'valid passports')
valid_passport.close()
    
