# Write a program that takes the email and password as input from a user and 
# checks if they are equal to “admin@mail.com” and password is “Admin@123” , 
# if so then print  “Login is Successful” and if not print “Invalid username or password”.
#  ONLY accept 3 tries after which it notifies you that you have been blocked.
# Once you learn functions,revisit this and write this code inside a function.

correct_email = "admin@mail.com"
correct_password = "Admin@123"

tries = 3

for i in range(tries):
    email = input("Enter email: ")
    password = input("Enter password: ")

    if email == correct_email and password == correct_password:
        print("Login is Successful")
        break
    else:
        tries = tries - 1 
        if tries > 0:
            value=f"Invalid username or password,{tries} tries left"
        else:
            value=f"{tries} tries left. You have been blocked"

print(value)