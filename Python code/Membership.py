#Check if the words contains specific letters, this is testing the membership operators

name = "Extreme"

print("x" in name)
print("E" in name)
print("e" not in name)

#Validate the following identity operands and they are stored in the same location

numb1 = 7
numb2 = 7
numb3 = 9

print(id(numb1))
print(id(numb2))
print(id(numb3))
print(numb1 is numb2)
print(numb1 is numb3)
print(numb2 is not numb3)