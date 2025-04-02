# Using Comma in string variables

username=input("Please enter your name: ")

print("Hello",username)

#Using the str.format

name=input("Enter your name: ")
age=input("Enter your age: ")

print("Hello, {}. You are {} years old".format(name,age))

#Using the f-string

name=input("Enter your name: ")

print(f"Hello, {name}!")