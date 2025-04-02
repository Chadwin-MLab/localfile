#Task
#Given an integer, , perform the following conditional actions:

#If x is odd, print Weird
#If x is even and in the inclusive range of 2 to 5, print Not Weird
#If x is even and in the inclusive range of 6 to 20 , print Weird
#If x is even and greater than 20 , print Not Weird

import math
import random
import re

x = int(input("Enter a number: "))
    
if (x % 2 ==0 and x > 20) or (x % 2==0 and 2<= x <=5):
    print("Not Weird")
elif (x % 2 !=0) or (x % 2==0 and   6 <=x <= 20):
    print("Weird")
    
else:
    print("Please try again with a valid input")