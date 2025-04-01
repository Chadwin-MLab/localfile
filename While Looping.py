# Using a while loop with if,elif statements

import random

generated_number = random.randint(1,10)

while True :
    try:
        user_guess=int(input("Enter your number between 1-10: " ""))
        
        if user_guess == generated_number :
            print("You guessed correctly")
            break # This exits the loop or the code will continue to retry until the number is guessed
        elif user_guess < generated_number : 
            print("Your guess is too low try again")
        else:
            print("Your guess is too high try again")
            
    
    except ValueError:
        print("Invalid input! Enter a number between 1-10")    
