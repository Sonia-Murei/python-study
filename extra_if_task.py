# 1.
# Write a program that checks login credentials:
# "Access granted" if email = "admin@gmail.com" and password = "Admin@123"
# "Wrong password" if email is correct but password is wrong
# "Email not found" otherwise

email="admin@gmail.com"
password="Admin@123" 

myemail=input("Enter email: ")
mypassword=input("Enter password: ")

if myemail==email and mypassword==password:
    print("Access granted")
elif myemail==email and mypassword !=password:
    print("Wrong password")
else:
    print("Email not found")

# 2.
# Create a program that validates an email:
# "Invalid email" if it does not contain "@" or "."
# "Gmail account" if it ends with "@gmail.com"
# "Other email provider" otherwise

email=input('Enter email: ')

if "@" not in email or "." not in email:
    print('Invalid email')
elif email.endswith("@gmail.com"):
    print('Gmail account')
else:
    print('Other email provider')

# 3.
# Write a program that checks password strength:
# "Weak" if length < 6
# "Moderate" if length 6–10 and contains at least one digit
# "Strong" if length > 10 and contains both digits and uppercase letters

password=input("Enter Password: ")

has_upper = any(char.isupper() for char in password)


if len(password) <6:
    print("Weak")
elif len(password) >=6 and len(password) <=10 and password.isalnum:
    print("Moderate")
elif len(password) >10 and password.isalnum and has_upper:
    print("Strong")
else:
    print("Weak")

# 4.
# Write a program that checks a password:
# "Invalid" if it does not start with a capital letter
# "Invalid" if it does not end with a number
# "Valid password" otherwise

password = input("Enter Password: ")

if not password[0].isupper():
    print("Invalid")
elif not password[-1].isdigit():
    print("Invalid")
else:
    print("Valid password")

# 5.
# Write a program that takes a number and checks:

# "Fizz" if divisible by 3
# "Buzz" if divisible by 5
# "FizzBuzz" if divisible by both
# Otherwise print the number

num = input("Enter a number: ")
num=int(num)

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

# 6.
# Create a program that takes a score and prints a grade:
# A (≥ 80)
# B (70–79)
# C (60–69)
# D (50–59)
# F (< 50)

score=input("Enter score: ")
score=int(score)

if score>=80:
    print('A')
elif score>=70 and score<80:
    print('B')
elif score>=60 and score<70:
    print('C')
elif score>=50 and score<60:
    print('D')
else:
    print('F')

# 7.
# Create a program that takes two numbers and prints:
# "Equal" if same
# "First is greater"
# "Second is greater"

num1=input("Enter num1: ")
num1=int(num1)
num2=input("Enter num2: ")
num2=int(num2)

if num1==num2:
    print('Equal')
elif num1>num2:
    print('First is greater')
else:
    print('Second is greater')

# 8.
# Write a program that takes a day number (1–7) and prints:
# Weekday (1–5)
# Weekend (6–7)
# Invalid input otherwise

day_number=input("Enter day number: ")
day_number=int(day_number)

if day_number>=1 and day_number<=5:
    print('Weekday')
elif day_number>=6 and day_number<=7: 
    print('Weekend')
else:
    print('Invalid input')

# 9.
# Create a program that takes a temperature and prints:
# "Freezing" if ≤ 0
# "Cold" if 1–15
# "Warm" if 16–30
# "Hot" if > 30

temp=input("Enter temperature: ")
temp=int(temp)

if temp>30:
    print('Hot')
elif temp>15 and temp<=30:
    print('Warm')
elif temp>=1 and temp<=15:
    print('Cold')
else:
    print('Freezing')


# 10.
# Create a program that takes a year and prints:
# "Leap year" if divisible by 4
# "Century year" if divisible by 100
# "Common year" otherwise

year=input('Enter year: ')
year=int(year)

if year%100 == 0 and year%400!=0:
    print('Century year')
elif year%4 == 0 or year%400==0:
    print('Leap year')
else:
    print('Common year')
