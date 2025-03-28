*Comments using python code*

It allows us to describe what each part of the code does.


-We use a # to specify Comments

#This is a comment 


-Make use of multi-line comments to comment out several lines of code:

"""
Line of code
to
comment
out

"""




*Working with Data in Python*

- Data is stored in memory and when we want to label it we call that a "variable"


- *What are variables*:
-The container in which we store data

-Variable name:declaring a label to the memory location
-Assigning the value using equals assignment operator
-Give the required value(Data needed to be stored)


- Rules for defining variables:
-Variable names should be meaningful and descriptive
-variable names should start with a letter or _underscore
-variable name cannot start with a number
-variable names are case sensitive so Country,country and COUNTRY are three different variables
-The value needs to be enclosed in quotes



- *Data Types*

-A variable is used to store any type of data required by an app
-Can be word, number, decimal, etc.
-EG

Name = "Frank"
age = 40
Temperature = 38.4

- Different data types:
-Numeric
-Sequence
-Boolean
-Sets
-Mapping Type


- *Working with numbers*

-Most common type of data are numeric, string and boolean

- Numeric:
-Integer: +, - or whole numbers and is represented as int
-Floating point: float, real numbers and are written as decimals
-Complex: can be expressed in the form a+b


- *Working with words*

-Most basic are strings

- Multi-line String:
-You can print multiple string using triple quotes: """ This quote is the one that should be printed """



- *True or False*

-Boolean: evaluating an expression that returns a value, yes or no, true or false. Also called bool.



- *Many times we want to know the type of data store in a variable. This is generally done for the debug and testing process*

-We use the type() function



- *Accepting User Input*

-Tracking a user or a specific calculation based on what the user is busy with
-Use the input() function to interact with users, to get data or a result.



*School Math in Python*

- *Operators in python*
-Arithmetic Operators
-Relational Operators
-Logical Operators
-Membership and identity Operator
-Bitwise Operators
-Walrus Operator



- Arithmetic Operators
-A math function that takes two operands and performs a calculation on them
-+ Addition
-(-) Subtraction
-*Multiplication
-/ Division of the left by right
-% Modulus divides left by right and returns the remainder
-** Exponent


- Comparison
-Are used for comparing value and either returns a true or false according to the condition
-> greater than
-< less than
-== equal to
-!= Not equal to
->= greater than or equal to
-<= less than or equal to


- Logical operators
-Is a symbol or word used to connect two or more expressions
-and : returns true is if both operands are true
-or : returns true if either of the operands are true
-not : returns true if the operand is false



- Membership and identity operators

-Membership operators
-in returns true if the value is found in the sequence
-not in returns true if the value is not found in the sequence

-Identity operators
-A variable name given to a memory location where a value is stored
-is returns True if the operands are identical
-not is returns True if the operands are not identical


- Walrus operator
-Used to assign variables within an expression using the notation
-:=
-Combines the steps of declaration
-for example 

name = "Sam"
print(name)

is the same as

print(name:=Sam)