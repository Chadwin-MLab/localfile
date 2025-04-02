#We have a list of appliance names and we want to iterate through it and fetch all the elements one by one.

appliances=["Dell", "Lenovo","Samsung","LG"]

#Now we iterate and check is a particular value is on the list and print it

for i in appliances:
    if i =="LG":
        print("LG found")
        break
else:
    print("LG not found")