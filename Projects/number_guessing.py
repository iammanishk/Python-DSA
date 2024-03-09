# ---------------------------- number gussing game (easy level) ----------------------------

import random

numberRange = int(input("Enter the range of the number you want to guess from 0 to: "))

if numberRange <= 0:
    print("Please enter a number greater than 0")
    quit()

guess = 0

while True:
    guess += 1
    user_guess = int(input(f"Guess the number between 0 and {numberRange}: "))
    randomNumber = random.randint(0, numberRange)
    print(randomNumber)
    if user_guess == randomNumber:
        print("You guessed it right!")
        break
    else:
        print("You guessed it wrong! Try again.")
        continue
print(f"You guessed it in {guess} times.")
    
   
    
