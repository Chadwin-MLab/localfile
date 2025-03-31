#Importing the random module

import random

#Generating a random number between 0 and 1

print(random.random())

#Generate a random number between 1 and 100

print(random.randint(1,100))

#Generate a random number between 1 and 10

print(random.randrange(1,10))

#Generate a random number between 1 and 10 with step size of 2

print(random.randrange(1,10,2))


#seed(x)- Initialize the random number generator

print(random.seed(1))
