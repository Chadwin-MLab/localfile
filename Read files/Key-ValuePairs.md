# Key Value Pairs(Dictionary)



# *What is a dictionary?*

- In a normal dictionary, keys are the words and values are the meanings of those words.

- It is another data structure in python.

- Some of the important features are:

-Unordered and mutable collection of items


-Each item has a key/value pair


-One can retrieve values when the key is known


-Each key is unique, values can be repeated


# *Structure of a Dictionary*

-Values can be of any type.


-keys must be of an immutable data type like strings, numbers or tuples


-Each key is separated from its value using a colon (:) and the whole value is enclosed in curly braces{}, elements are separated using commas

-Example: dict1= {1:"Human",2: "Sam"}
                print(dict1)

# *Manipulating dictionaries*

-Cannot be done using index(i) as it is unordered.

-We instead use the keys to identify values


# *Dictionary functions*

-keys()returns a list of keys in the dictionary


-values()returns the list of dictionary values



-clear()removes all the elements of the dictionary


-get(key)returns the value of the specified key.

-items()returns a list of dictionaries key-value pairs in tuple form

-update()adds specified key-value pairs to the dictionary