# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 00:15:00 2021

@author: saira

"""

# Date:              12 November 2021
#interest calculate
file_name = str(input("Please enter the output filename: "))
P = float(input("Please enter the principal amount: "))
N = float(input("Please enter the term length (months): "))
i = float(input("Please enter the annual interest rate: "))


J = i/12

M = (P * J)/(1-(1/(1+J))**N)

#print(M)
with open(file_name, 'w') as loan:
    #print(loan)
   # print('Month, Total, Accured Interest, Loan Balance')
    Header = 'Month' + ',' + 'Total Accrued Interest' + ',' + 'Loan Balance'
    loan.write(Header)
    #loan.write('Month, Total Accured Interest, Loan Balance\n')
    month = 0
    beginning = 0
    balance = 0
    month_int = 0
    while P > 0:
        loan.write('{},${:.2f},${:.2f}\n'.format(month,month_int,P))
        month_i = J * P
        P = (month_i + P) - M
        month += 1
        beginning = balance
        month_int += month_i
    if P < 0:
        P = -P
    loan.write('{},${:.2f},${:.2f}\n'.format(month, month_int, P))
       # print(month, month_i, P)
        
