#Create a number guessing game

#Importing the random module first

import random

#Generate a random number in the rand 1-10

generatedNumber=random.randrange(1,10)

userGuess=int(input("Guess a number between 1-10: "))

if userGuess==generatedNumber:
    print("You have guessed correctly")
elif userGuess<generatedNumber:
    print("Your guess us too low")
else:
    print("Your guess is too high")