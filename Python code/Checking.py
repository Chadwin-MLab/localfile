#In the below code we will print a list of countries, del a country and to see if the country deleted is still in the list

countries=["Brazil","SA","Ghana","Mos","Nigeria","Spain","Zim","Lesotho"]

del countries[0], countries[4]

print(countries)

if ("Brazil" and "Spain" in countries):
    print("Countries not deleted appropriately")
else:
    print("All in order")