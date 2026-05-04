# Write a program which accepts email as form input or from terminal. 
# Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.
# Once you learn functions,revisit this and write this code inside a function.

email=input('Enter email: ')

if "@" not in email or "." not in email:
    res=f'{email} is an invalid email.'
else:
    res=f'{email} is a valid email.'

print(res)

# Using functions:

def validate_email(email):
    if "@" not in email or "." not in email:
        res=f'{email} is an invalid email.'
    else:
        res=f'{email} is a valid email.'
    return res

email=input('Enter email: ')
result=validate_email(email)