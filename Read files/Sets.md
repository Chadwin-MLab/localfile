# Sets in Python

- Set is a data structure in Python that is used to group and store multiple elements

- Sets are unordered collections.

- Set elements are unique. Meaning no duplicates are allowed.

- A set can be manipulated but the elements must be immutable.

# *Created*

- It is created by using the set() function for empty set or placing all the elements within a pair of curly braces{}

# *Accessing elements*

- A collection data type.

- It is unordered therefore we gather data by looping through the set

-Example

weekdays={"Monday","tuesday","wednesday"}

for Mon in weekdays:
    print(Mon)

# *Sets Operations*

- Union of Sets

-We can join two sets/combine them to contain a new set of elements using the | operator or using the union() method

-Lets join two sets A and B

A={1,2,3}
B={2,3,4}

print(A | B)

or 

print(A.union(B))



- Set Intersection

-Finding commonalities or places where the sets overlap.
-Can be performed using the & operator or the intersection() method.



- Difference of Sets

We use the - operator or the difference() method.

