# Write a program called stars. It should prompt the user for a number, 
# and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....
# Once you learn functions,revisit this and write this code inside a function.

rows = int(input("Enter number of rows: "))

for i in range(rows):
    print("*" * (i + 1))
