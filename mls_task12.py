# Write a program that prints the largest of 4 inputs taken as input from a user.
# Once you learn functions,revisit this and write this code inside a function.

num1=input("Enter num1: ")
num1=int(num1)
num2=input("Enter num2: ")
num2=int(num2)
num3=input("Enter num3: ")
num3=int(num3)
num4=input("Enter num4: ")
num4=int(num4)

if num1>num2 and num1>num3 and num1>num4:
    ret=f'{num1} is the largest'
elif num2>num1 and num2>num3 and num2>num4:
    ret=f'{num2} is the largest'
elif num3>num1 and num3>num2 and num3>num4:
    ret=f'{num3} is the largest'

print(ret)

# Using functions:
def largest_number(num1,num2,num3,num4):
    if num1>num2 and num1>num3 and num1>num4:
        large=num1
    elif num2>num1 and num2>num3 and num2>num4:
        large=num2
    elif num3>num1 and num3>num2 and num3>num4:
        large=num3
    else:
        large=num4
    return large

input1=input("Enter 1st number: ")
input1=int(input1)  
input2=input("Enter 2nd number: ")
input2=int(input2)
input3=input("Enter 3rd number: ")
input3=int(input3)
input4=input("Enter 4th number: ")
input4=int(input4)

largest=largest_number(input1,input2,input3,input4)
print(f'Largest number: {largest}')
