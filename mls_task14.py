# Write a program that takes input of 2 values and adds them. 
# The program should only accept numbers and floats only 
# or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
# Once you learn functions,revisit this and write this code inside a function.

while True:
    try:
        a = float(input("Enter first value: "))
        b = float(input("Enter second value: "))
        result = a + b
        print("Sum:", result)
        break
    except:
        print("invalid character entered")

