# We will specify a list and use a few functions on the list

names=["John","Joe","Frank","Leroy"]

#Lets use the append method to add a name at the end of the list

print(names)

names.append("Barry")

print(names)

#Lets use the insert method to insert a name at the specified index

names.insert(2,"Human")

print(names)

#Now lets use the pop element to reverse and remove the last element from the list

names.pop()

print(names)

#Now lets remove a specific element from the list

names.remove("Joe")

print(names)

#Lets reverse the order of items on the list

names.reverse()

print(names)

#Lets use the index method to return the index of the selected element

print(names.index("Human"))