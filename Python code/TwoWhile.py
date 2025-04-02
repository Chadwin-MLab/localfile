# Using another example of a while loop

people = 3

while True: 
    try:
        if people == 10:
            print("Your mini bus is full")
            break
        elif people <= 5 :
            print("Your minibus is empty")
            
            people += 1
        else:
            print("Your minibus is not at capacity yet")

            people += 1
    
    except ValueError:
        print("Invalid Input")         