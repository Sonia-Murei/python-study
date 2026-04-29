1.# write a program that takes users age as input
# if the age is 18 and above ,check if they have  drivers license if they do we print you are eligible to drive
# if they dont have a drivers license print you are not eligible to drive
# otherwise you are too young to drive

age=int(input("Enter your age: "))

if age>=18:
    license=input("Do you have a driver\'s license? yes or nor? ")
    if license=="yes":
        print("you are eligible to drive")
    else:
        print("you are not eligible to drive")
else:
    print("you are too young to drive")

2.# Write a program that:
# = > Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above 50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low."

credit_score=int(input("Enter your credit score: "))
income=float(input("Enter your annual income: " ))

if credit_score>700:
    if income>50_000:
        print("Loan approved")
    else:
        print("Income requirement not met")
else:
    print("Credit score too low")

# Write a program that:
# Takes a transaction amount and account type ("Standard" or "Premium") as input.
# If the account type is "Standard":
# Check if the amount is above 500:
# If it is, print "Transaction exceeds the limit for Standard accounts."
# If not, print "Transaction approved."
# If the account type is "Premium":
# Check if the amount is above 1,000:
# If it is, print "Transaction exceeds the limit for Premium accounts."
# If not, print "Transaction approved."
# otherwise wrong account type.

account_type=input("Enter account type (Standard/Premium: )").title()
transaction_amount=float(input("Enter transaction amount: "))

if account_type=="Standard":
    if transaction_amount>500:
        print("Transaction exceeds the limit for Standard accounts.")
    else:
        print("Transaction approved.")
elif account_type=="Premium":
    if transaction_amount>1000:
        print("Transaction exceeds the limit for Premium accounts.")
    else:
        print("Transaction approved.")
else:
    print("wrong account type.")

