*Making Decisions we use conditionals*

- *Conditional Statements in python are* :

-If Statement
-If-else statement
-If-elif-else statement
-Nested If-else statement

- *If Statement*
-Used to check whether a condition is True or False.
-if the condition is true then only the statements under the if statements will execute,otherwise, they will be ignored and statements outside of the if block are executed.
-Example

if condition:
   #Statements to be executed if the condition is True

if is the keyword. The colon: is used to make the code more readable. The statements to be executed are added under the if statement and indented.


- *If-Else Statement*
-The else statement will be evaluated, if the boolean expression tested by the if block is false.
-Example

if condition:
   #Statement is true
else:
   #Statement is false   


- *Understanding indentation*
-Adding a white space before a statement
-Helps the code executor understand which code to execute next.
-(Indentation Error) when there isn't proper indentation.
-Use tab or space to indent your code


- *Handling multiple conditions*
-When handling more then one condition we use the if-elif-else statement
-Example

if condition:
    #Statement True
elif condition2:
    #Statement True
elif condition3:
    #Statement True
else:
    False

- *Nested If statments*
-Checking for another condition are a condition is already true.
-You can have and if, elif, else constructs