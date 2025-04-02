# Given the 3 sides of a triangle - x, y and z - determine whether the triangle is equilateral, isosceles or obtuse.

# Note: Equilateral means all sides are equal, isosceles means two of the sides are equal but not the third one, obtuse means all 3 are different.

import math

x=int(input("Enter a value of the x side of a triangle: "))

y=int(input("Enter the value for the y side of the triangle: "))

z=int(input("Enter a value for the z side of the triangle :"))


if x==z and x==y:
    print("Equilateral")
elif x==y or y==z  or x==z:
    print("Isosceles")
else:
    print("Obtuse")  