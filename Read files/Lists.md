# *List*

- Allows us to store a list of values, and we can access them individually using the concept of index numbers.

- Data type/structure in python


# *Features of lists*

- Lists are ordered collections of multiple values.

- Lists are mutable, can be changes and manipulated over a period of time

- Allow us to store duplicate values

# *How to create*

- By placing the sequence inside the square brackets [].

- The elements are comma-separated.

- Can have any number of items and they may be of different types(integer, float,string, etc)

# *Manipulating lists*

- *Accessing elements of a list*

-Since it is a sequence data type, we can access elements using indices.

-Like strings lists are assigned an index starting from zero.




- *List Slicing*

-Works the same way as strings

-cars=[bmw,vw,ford]

-print(cars[0:1]), will print bmw and vw




- *Updating a list*

-we have a list of student marks=[50,20,36,72,90]

-Now lets say the student with 20 is a mistake and we need to update the list to 60

-we do it like:

-marks[1]=60 #use the index of the mark you wish to update

-print(marks)

- *Deleting elements from a list*

-if we know the index of the number of the element we wish to delete from the list, we can use the del statement

-example

-names=[john, joe, juju]

-print(names)

-del names[0] # deleting johns name

-print(names)

# *Basic operations on lists*

- List Concatenation and Repetition

- Adding two lists is concatenation and multiplying a list is repetition.

- We can use + and * operators respectively

-example:
-lst1=[1,2,3]
-lst2=[x,y,z]

print(lst1+list2)

print(lst1 * 3)


- the (in) operator is used to test membership

-enrolledList =["Sam","Chad","Kane"]

-print("Sam" in enrolledList)

-print("Chadwin" in enrolledList)

# *Iterating over lists*

- We can use the concept of loops to iterate over the sequence.

- It is a fixed number of iterations therefore we use a for loop.

# *List Methods*

-append(element):Adds the specified element to the end of the list

-insert(index,element):inserts and element at the specified index

-pop()removes and returns the last element from the list

-remove(element)removes the specified element from the list

-reverse()reverse the order of items in the list

-index(element)returns the index of the first matched item

-count(element)returns count of how many times an element occurs in the list