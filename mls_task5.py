# Implement a program that takes 3 users  inputs from the terminal or the Browser, 
# and stores them in three variables. Return the largest of the three. 
# Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 

num1=input("Enter num1: ")
num1=int(num1)
num2=input("Enter num2: ")
num2=int(num2)
num3=input("Enter num3: ")
num3=int(num3)

if num1>num2 and num1>num3:
    ret=f'{num1} is the largest'
elif num2>num1 and num2>num3:
    ret=f'{num2} is the largest'
else:
    ret=f'{num3} is the largest'

print(ret)