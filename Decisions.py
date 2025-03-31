#An If statement to evaluate if a user is above the age of 18 in order to vote, if statement only handles true path

age=int(input("Enter your age"))
if age>=18:
    print("Congratulation, your are eligible to vote")
    
    
#Now lets add a false path, or an else path so if it does not meet the criteria

speed=int(input("Enter the speed"))
if speed<=120:
    print("Not Speeding fine")
else:
    print("You are in breach and will receive a speeding fine")    
    
