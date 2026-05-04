# Write a program that lets the user input a password. 
# Give them only 4 attempts to check the passwords entered against “admin@123”. 
# If the password is correct access is granted. 
# After you show them a message , the account is blocked.
# Once you learn functions,revisit this and write this code inside a function.

tries=4
attempts=list(range(1,4))

for i in attempts:
	pin=input('Enter pin:')
	correct_pin='admin@123'
	if pin==correct_pin:
		print("Welcome")
		break
	else:
		remaining_tries=tries-i
		if remaining_tries>0:
			print(f'incorrect pin try again {remaining_tries} tries remaining')
		else:
			print("account Blocked")