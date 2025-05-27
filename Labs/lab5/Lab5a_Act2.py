# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 18:27:40 2021

@author: saira

"""

# Date:              30 September 2021
#


# inputs 
sex = input("Enter your sex (M/F): ")
age = float(input("Enter your age (years): "))
smoke = input("Do you smoke cigarettes (Y/N)? ")
total_chol = float(input("Enter your total cholesterol (mg/dL): "))
hdl = float(input("Enter your HDL cholesterol (mg/dL): "))
BP = float(input("Enter your systolic BP (mmHg): "))
med = input("Are you taking blood pressure medication (Y/N)? ")
points = 0
ten_year_risk = 0

# if patient is male
if sex == "M" or sex =="m":
    # how old is the patient?
    if 20 <= age <= 34:
      points += -9
    elif 35 <= age <= 39:
        points += -4
    elif 40 <= age <= 44:
        points += 0    
    elif 45 <= age <= 49:
        points += 3   
    elif 50 <= age <= 54:
        points += 6   
    elif 55 <= age <= 59:
        points += 8  
    elif 60 <= age <= 64:
        points += 10 
    elif 65 <= age <= 69:
        points += 11 
    elif 70 <= age <= 74:
        points += 12 
    elif 75 <= age <= 79:
        points += 13
     

    # total cholesterol
    if 20 <= age <= 39:  
      if total_chol < 160:
          points += 0
      elif 160 <= total_chol <= 199:
          points += 4
      elif 200<= total_chol <= 239:
          points += 7
      elif 240 <= total_chol <= 279:
          points += 9
      elif total_chol >= 280:
          points += 11
    elif 40 <= age <= 49:
        if total_chol < 160:
            points += 0
        elif 160 <= total_chol <= 199:
            points += 3
        elif 200 <= total_chol <= 239:
            points += 5
        elif 240 <= total_chol <= 279:
            points += 6
        elif total_chol >= 280:
            points += 8
    elif 50 <= age <= 59:
        if total_chol <160:
            points += 0
        elif 160 <= total_chol <= 199:
            points += 2
        elif 200 <= total_chol <= 239:
            points += 3
        elif 240 <= total_chol <= 279:
            points += 4
        elif total_chol >= 280:
            points +=5
    elif 60 <= age <= 69:
        if total_chol < 160:
            points += 0
        elif 160 <= total_chol <= 199:
            points += 1
        elif 200 <= total_chol <= 239:
            points += 1
        elif 240 <= total_chol <= 279:
            points += 2
        elif total_chol >= 280:
            points += 3
    elif 70 <= age <= 79:
        if total_chol < 160:
            points += 0
        elif 160 <= total_chol <= 199:
            points += 0
        elif 200 <= total_chol <= 239:
            points += 0
        elif 240 <= total_chol <= 279:
            points += 1
        elif total_chol >= 280:
            points += 1
            
            
    # smoke or not 
    if 20 <= age <= 39:
        if smoke == "n":
            points += 0
        elif smoke == "y":
            points += 8
    if 40 <= age <= 49:
        if smoke == "y":
            points += 5
        elif smoke == "n":
            points += 0
    if 50 <= age <= 59:
        #age = age
        if smoke == "y":
            points += 3
        elif smoke == "n":
            points += 0
    if 60 <= age <= 69:
        if smoke == "y":
            points += 1
        elif smoke == "n":
            points += 0
    if 70 <= age <= 79:
        if smoke == "y":
            points += 1
        elif smoke == "n":
            points += 0
            
    # HDL 
    if hdl >= 60:
        points += -1
    elif 50 <= hdl <= 59:
        points += 0
    elif 40 <= hdl <= 49:
        points += 1
    elif hdl < 40:
        points += 2
    
    # bp med
    if med == "n":
        if BP < 120:
            points += 0
        elif 120 <= BP <= 129:
            points += 0
        elif 130 <= BP <= 139:
            points += 1
        elif 140 <= BP <= 159:
            points += 1
        elif BP >= 160:
            points += 2
    elif med == "y":
        if BP < 120:
            points += 0
        elif 120 <= BP <= 129:
            points += 1
        elif 130 <= BP <= 139:
            points += 2
        elif 140 <= BP <= 159:
            points += 2
        elif BP >= 160:
            points += 3

    # totaling points 
    if points < 0:
        ten_year_risk = str(ten_year_risk)
        ten_year_risk = "<1"
    elif points == 0:
        ten_year_risk = 1
    elif points == 1:
        ten_year_risk = 1
    elif points == 2:
        ten_year_risk = 1
    elif points == 3:
        ten_year_risk = 1
    elif points == 4:
        ten_year_risk = 1
    elif points == 5:
        ten_year_risk = 2
    elif points == 6:
        ten_year_risk = 2
    elif points == 7:
        ten_year_risk = 3
    elif points == 8:
        ten_year_risk = 4
    elif points == 9:
        ten_year_risk = 5
    elif points == 10:
        ten_year_risk = 6
    elif points == 11:
        ten_year_risk = 8
    elif points == 12:
        ten_year_risk = 10
    elif points == 13:
        ten_year_risk = 12
    elif points == 14:
        ten_year_risk = 16
    elif points == 15:
        ten_year_risk = 20
    elif points == 16:
        ten_year_risk = 25
    elif points >= 17:
        ten_year_risk = str(ten_year_risk)
        ten_year_risk = ">30"
        


# if patient is female
if sex == "f" or sex == "F":
    # how old is the patient?
    if 20 <= age <= 34:
      points += -7
    elif 35 <= age <= 39:
        points += -3
    elif 40 <= age <= 44:
        points += 0    
    elif 45 <= age <= 49:
        points += 3   
    elif 50 <= age <= 54:
        points += 6   
    elif 55 <= age <= 59:
        points += 8  
    elif 60 <= age <= 64:
        points += 10 
    elif 65 <= age <= 69:
        points += 12 
    elif 70 <= age <= 74:
        points += 14
    elif 75 <= age <= 79:
        points += 16
     

    # total cholesterol
    if 20 <= age <= 39:  
      if total_chol < 160:
          points += 0
      elif 160 <= total_chol <= 199:
          points += 4
      elif 200<= total_chol <= 239:
          points += 8
      elif 240 <= total_chol <= 279:
          points += 11
      elif total_chol >= 280:
          points += 13
    elif 40 <= age <= 49:
        if total_chol < 160:
            points += 0
        elif 160 <= total_chol <= 199:
            points += 3
        elif 200 <= total_chol <= 239:
            points += 6
        elif 240 <= total_chol <= 279:
            points += 8
        elif total_chol >= 280:
            points += 10
    elif 50 <= age <= 59:
        if total_chol <160:
            points += 0
        elif 160 <= total_chol <= 199:
            points += 2
        elif 200 <= total_chol <= 239:
            points += 4
        elif 240 <= total_chol <= 279:
            points += 5
        elif total_chol >= 280:
            points += 7
    elif 60 <= age <= 69:
        if total_chol < 160:
            points += 0
        elif 160 <= total_chol <= 199:
            points += 1
        elif 200 <= total_chol <= 239:
            points += 2
        elif 240 <= total_chol <= 279:
            points += 3
        elif total_chol >= 280:
            points += 4
    elif 70 <= age <= 79:
        if total_chol < 160:
            points += 0
        elif 160 <= total_chol <= 199:
            points += 1
        elif 200 <= total_chol <= 239:
            points += 1
        elif 240 <= total_chol <= 279:
            points += 2
        elif total_chol >= 280:
            points += 2
            
            
    # smoke or not 
    if 20 <= age <= 39:
        if smoke == "n":
            points += 0
        elif smoke == "y":
            points += 9
    if 40 <= age <= 49:
        if smoke == "y":
            points += 7
        elif smoke == "n":
            points += 0
    if 50 <= age <= 59:
        #age = age
        if smoke == "y":
            points += 4
        elif smoke == "n":
            points += 0
    if 60 <= age <= 69:
        if smoke == "y":
            points += 2
        elif smoke == "n":
            points += 0
    if 70 <= age <= 79:
        if smoke == "y":
            points += 1
        elif smoke == "n":
            points += 0
            
    # HDL 
    if hdl >= 60:
        points += -1
    elif 50 <= hdl <= 59:
        points += 0
    elif 40 <= hdl <= 49:
        points += 1
    elif hdl < 40:
        points += 2
    
    # bp med
    if med == "n":
        if BP < 120:
            points += 0
        elif 120 <= BP <= 129:
            points += 1
        elif 130 <= BP <= 139:
            points += 2
        elif 140 <= BP <= 159:
            points += 3
        elif BP >= 160:
            points += 4
    elif med == "y":
        if BP < 120:
            points += 0
        elif 120 <= BP <= 129:
            points += 3
        elif 130 <= BP <= 139:
            points += 4
        elif 140 <= BP <= 159:
            points += 5
        elif BP >= 160:
            points += 6

    # totaling points 
    if points < 9:
        ten_year_risk = str(ten_year_risk)
        ten_year_risk = "<1"
    elif points == 9:
        ten_year_risk = 1
    elif points == 10:
        ten_year_risk = 1
    elif points == 11:
        ten_year_risk = 1
    elif points == 12:
        ten_year_risk = 1
    elif points == 13:
        ten_year_risk = 2
    elif points == 14:
        ten_year_risk = 2
    elif points == 15:
        ten_year_risk = 3
    elif points == 16:
        ten_year_risk = 4
    elif points == 17:
        ten_year_risk = 5
    elif points == 18:
        ten_year_risk = 6
    elif points == 19:
        ten_year_risk = 8
    elif points == 20:
        ten_year_risk = 11
    elif points == 21:
        ten_year_risk = 14
    elif points == 22:
        ten_year_risk = 17
    elif points == 23:
        ten_year_risk = 22
    elif points == 24:
        ten_year_risk = 27
    # elif points == 25:
    #     ten_year_risk = 25
    elif points >= 25:
        ten_year_risk = str(ten_year_risk)
        ten_year_risk = ">30"
        
    
    
    
    
        
            
        
            


ten_year_risk = str(ten_year_risk)

#print(points)
print("Your 10-year risk of a heart attack is " + ten_year_risk + "%")
    
