#Creating a simple function to say hello

def say_hello():
    print("Hello")
    
say_hello()


#Creating a simple function with parameters

def say_greetings(name):
    print("Hello", name)
    
    
say_greetings("Chad")

#Creating a function that will add two numbers

def addnumbers(num1,num2):
    num3=num1+num2
    return num3

print(addnumbers(12,8))