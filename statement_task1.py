# 1.Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.
num1=input('Enter the first number: ')
num1=int(num1)
num2=input('Enter the second number: ')
num2=int(num2)
num3=input('Enter the third number: ')
num3=int(num3)

if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)

# Take four inputs from a user, separately. Print the largest of the numbers.
num1=input('Enter the 1st number: ')
num1=int(num1)
num2=input('Enter the 2nd number: ')
num2=int(num2)
num3=input('Enter the 3rd number: ')
num3=int(num3)
num4=input('Enter the 4th number: ')
num4=int(num4)

if num1>num2 and num1>num3 and num1>num4:
    print(num1)
elif num2>num1 and num2>num3 and num2>num4:
    print(num2)
elif num3>num1 and num3>num2 and num3>num4:
    print(num3)
else:
    print(num4)

# 2.Take as input from a user the temperature 
# if the temperature is above 30°C display “The temperature is too high”,
# if the temperature is above 15 display “Normal temperature” 
# otherwise display “Cold temperature”
temp=input("Enter temperature: ")
temp=int(temp)

if temp>30:
    print('The temperature is too hot')
elif temp>15 and temp<30:
    print('Normal temperature')
else:
    print('Cold temperature')

# Create a program that checks the user's balance:
# "Insufficient funds" if <100
# "Moderate Balance" if 100-1000
# "High Balance" if >1000
balance=input("Enter balance: ")
balance=int(balance)

if balance < 100:
    print("Insufficient funds")
elif balance >=100 and balance<=1000:
    print("Moderate Balance")
else:
    print("High Balance")

# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. 
# If both conditions are true, print "Conditions met", 
# otherwise print "Conditions not met"
x=input("Enter x: ")
x=int(x)
y=input("Enter y: ")
y=int(y)

if x<=20 and x>=10 and y>100:
    print('Conditions met')
else:
    print('Conditions not met')

# Write a program that checks:
# "Small" if number <10
# "Medium" if 10-50
# "Large" if >50
number=input("Enter number: ")
number=int(number)

if number<10:
    print("Small")
elif number>=10 and number<=50:
    print("Medium")
else:
    print("Large")
# # 4. Write a Python program that checks if a variable password is equal to the string "secret123". 
# If it is, print "Access   granted", 
# otherwise print "Access denied"
password="secret123"
mypassword=input("Enter Password: ")

if mypassword==password:
    print('Access granted')
else:
    print('Access denied')

#  Write a program that asks the user for email and password 
# checks if the email is equal to "admin@gmail.com" 
# and passaword is equal to "admin123" 
# if it is print Access granted otherwise print Access Denied.

email="admin@gmail.com"
password="admin123" 

myemail=input("Enter email: ")
mypassword=input("Enter password: ")

if myemail==email and mypassword==password:
    print("Access granted")
else:
    print("Access denied")

# 5. Write a Python program that checks if a variable student_score is greater than 90. 
# If true, check if the attendance is greater than 80. 
# If both conditions are true, print "Excellent student", 
# otherwise print "Good score, but attendance needs improvement"
student_score=92
attendance=85


if student_score>90:
    if attendance>80:
        print('Excellent student')
    else:
        print('Good score, but attendance needs improvement')