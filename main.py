#Activity 1: Take a number as input from user in a given interval. Also take a random number from the computer in the same interval. If the user input is greater than random number then display "You Won" otherwise display "You lose"

a = int(input("Enter your number between 1 to 100: "))
print(a)

import random
b = random.randint(1,100)
print(b)

if(a>b):
  print("You won")
else:
  print("you loss")
