# *First Step* the enter products function

"""

- Accept the name of the product purchased by the customer.

- Accept the quantity of the product purchased.

- The process will need to be looped until all the products are entered.

"""
#Showing the customer a List of products available for purchase
viewProducts=["Biscuit","Chicken","Egg","Fish","Coke","Bread","Apple","Onion"]

print("These are the products available for purchase", viewProducts)




def enterProducts():                                                        #Name of the function and does not take any parameters
    buyingData = {}                                                         #Our data structure, data dictionary that will be empty
    enterDetails = True
    while enterDetails:                                                     #Our while loop until all products are entered
        details = input("Press A to add a product and Q to quit: ")
        if details == "A":                                                  
            product = input("Enter product: ")
            quantity =int(input("Enter quantity: "))
            buyingData.update({product:quantity})                           #Adding products to our dictionary
        elif details == "Q":
            enterDetails= False
        else:
            print("Please select a correct option")                         # Error message if A or Q is not entered
    return buyingData


# Calculating the total price of our products

def getPrice(product, quantity):                                           # Our get price function that accepts product and quantity, this value will come from the previous function
    priceData = {                                                          #Data dictionary with product as the key and price as the value
        "Biscuit":3,
        "Chicken":5,
        "Egg":1,
        "Fish":3,
        "Coke":2,
        "Bread":2,
        "Apple":3,
        "Onion":3
    }
    
    subtotal=priceData[product] * quantity
    print(product+":$"+str(priceData[product])+"x"+str(quantity)+ "=" + str(subtotal))
    return subtotal
    

#Now we check if the customer is a member and give discount based on that

def getDiscount(billAmount,membership):
    discount = 0
    if billAmount >=25:
        if membership == "Gold":
            discount = 20
        elif membership == "Silver":
            discount = 10
        elif membership =="Bronze":
            discount = 5
        else:
            discount = 0
            
        discountAmount = billAmount * (discount/100)
        finalAmount =billAmount -discountAmount
        
                
        print(f"{discount}% off for {membership} membership: -${discountAmount:.2f}")
        return finalAmount
    
    else:
        print("No discount on amount less than $25")
    return billAmount

# Now we need to print the final bill for the customer

def makeBill(buyingData,membership):
    billAmount = 0
    for key, value in buyingData.items():
        billAmount+= getPrice(key,value)
    billAmount = getDiscount(billAmount,membership)
    print("The discounted amount is $" + str(billAmount))            
    
    
#Now we need our boilerplate, this is to call our functions

buyingData = enterProducts()
membership = input("Enter customer membership: ")
makeBill(buyingData, membership)