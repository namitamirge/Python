# importing the random module
import random

## this is the dice game
#user will roll the dice
#
print('Hey, whats your name?')
name=input()
print('Please roll the dice ' +name)
print('How many times do you wanat to roll?')

i=1
while i< 6:
      roll=int(input())

      print(random.randint(0,6)) 
      break

i+=1
