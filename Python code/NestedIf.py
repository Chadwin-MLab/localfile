# Here is a code example that checks if the username and password match to be able to log into a system

username=input("Enter your username: ")
password=input("Enter your password: ")

if username=="John":
    if password== "12345":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("User not found")