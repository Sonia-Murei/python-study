# 1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
# If start_date comes before end_date, print "Valid period",
# If start_date is after end_date, print "Invalid period".
# If both dates are the same, print "One-day period".

start_date = '2024-01-01'
end_date = '2024-12-31'

if start_date<end_date:
    print("Valid period.")
elif start_date>end_date:
    print("Invalid period.")
else:
    print("One-day period.")

# "nested if" answer

# start_date = '2024-01-01'
# end_date = '2024-12-31'

# if start_date < end_date:
#     print("Valid period.")
# else:
#     if start_date > end_date:
#         print("Invalid period.")
#     else:
#         print("One-day period.")

# 2.Given two strings str1 and str2, write a conditional statement that checks:
# If str1 is longer than str2, print "str1 is longer".
# If str2 is longer than str1, print "str2 is longer".
# If both have equal length, print "Both are of equal length".

str1=int(input("Enter string 1 length: "))
str2=int(input("Enter string 2 length: "))

if str1 > str2:
    print("str1 is longer.")
elif str2 > str1:
    print("str2 is longer.")
else:
    print("Both are of equal length.")

# "nested if" answer
# if str1 > str2:
#     print("str1 is longer.")
# else:
#     if str2 > str1:
#         print("str2 is longer.")
#     else:
#         print("Both are of equal length.")

# 3.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
# Prints "Access Granted" if user_id is in valid_ids.
# Prints "Access Denied" if user_id is not in valid_ids.

valid_ids = [101, 102, 103]
user_id = 105

if user_id in valid_ids:
    print("Access Granted")
else:
    print("Access Denied")

# 4.Given a variable value that could be of any type, write a conditional statement that:
# Prints "String Detected" if value is a string.
# Prints "Integer Detected" if value is an integer.
# Prints "Unknown Type" for any other type.
    
value = input("Enter a value: ")

if isinstance(value, str):
    print("String Detected")
elif isinstance(value, int):
    print("Integer Detected")
else:
    print("Unknown Type")

    # Alternative Answer:

value=10

if type(value)==str:
    print("String Detected")
elif type(value)==int:
    print("Integer Detected")
else:
    print("Unknown Type")

# 5.Given x = 7 and y = 14, write nested conditional statements that print:
# "x and y are both even" if both x and y are even numbers.
# "Only y is even" if only y is even.
# "Neither x nor y are even" if both are odd.

x=7
y=14

if x % 2 == 0:
    if y % 2 == 0:
        print("x and y are both even.")
else:
    if y % 2 == 0:
        print("Only y is even.")
    else:
        print("Neither x nor y are eve.n")