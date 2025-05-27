# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:57:01 2021

@author: saira

"""

# Date:              29 November 2021
#number guessing game
import random


 # is the guess to0 high? too low? or just right?
def high(guess, number):
    count()
    # call count function 
    # run the input through the guess function
    if guess > number:
        return "Too high!"
    elif guess < number:
        return "Too low!"
    elif guess == number: # if guess = number then break function 
        return 'break'
def count(number):
  count = 0
  while True:
      guess = int(input("What is your guess? "))
      count += 1  
      condition = high(guess, number)
      
      if condition == 'break':
          break # break if condition == 'break'
      else:
         print(condition)
  return count # return count
      

# main functiuon 

def main():
    print("Guess the secret number! Hint: it's an integer between 1 and 100...")
    number = random.randint(1,100) # pick a random number from 1 to 100
    amount = high(number)
    print("You guess it! It only took {} guesses.".format(amount))
if __name__=='__main__':
    main() 
