"""
Grading system, 

If marks are greater than or equal to 90, then Excellent

if marks are less than 90 and greater or equal to 75, grade is first class

if marks are less than 75 and greater or equal to 40, grade is average

if marks are less than 40, grade is fail

"""

marks=int(input("Enter your grade: "))

if marks>=90:
    print("Grade is Excellent")
elif marks<90 and marks>=75:
    print("Grade is first class")
elif marks<75 and marks>=40:
    print("Grade is average")
else:
    print("Grade is a fail")



