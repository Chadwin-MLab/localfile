# *Working with Strings*

- *String formatting*

-using values of variables in our strings to print something or generate a customized string

-for example we would like to generate, "Hello John" by accepting input from the user rather than just printing "Hello, User"

- *Using comma*

-Is generally used when we want to format a string and use the value of the variable at the end


- *Using str.format*

-The format() method formats the specified values and inserts them inside the string's placeholder.
-Placeholder is defined using curly brackets


- *fstrings*
-A way to embed expressions inside string literals, using minimal syntax.


- *Assessing strings*

- Concept of Index

-An index is a numerical representation of an item's position in a sequence.
-The sequence can be a list, string of characters, or any arbitrary sequence of values.


- *Slicing in python*

-Slicing is about obtaining a sub-string from the given string by slicing it respectively from start to end
string[start:end:step]

- *Concatenation*

-Adding two strings
-Can be done using:
-+ Operator
-join() method

- *String Repetition*

-*Operator is used for performing string repetition.
-str ="Python"
-print(str*2)

-result= PythonPython


- *String Methods*

-capitalize()-Converts the first letter to uppercase and all others to lowercase
-count(x)-returns the number of times a specified value occurs in a string
-find(x)-searches the string for a specified value and returns the position where it was found, if not found will return a -1
-isalnum()-returns true if all characters in the string are alphanumeric