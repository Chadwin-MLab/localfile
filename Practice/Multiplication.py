# Write out the timetable for a given number

import math
import random
import re

a=int(input("Please provide a number for which you would like a timetable for: "))

print(f"Multiplication Table for{a}: ")

for i in range(1,13):
    print(f"{a} x {i} = {a * i}")