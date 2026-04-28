# GROUP 1
# Q1
# A bank wants to improve its ATM service. Create a program that
# stores a customer’s name and account balance, then allows them to
# request a withdrawal. If the amount requested is greater than the
# available balance, the transaction should fail. If successful, deduct the
# amount together with a transaction fee of KES 30 and display the new
# balance.

customer_name = input("Enter customer name: ")
account_balance = 100000
amount_requested = input("Enter the amount to withdraw: ")
amount_requested = int(amount_requested)

trans = 30

if amount_requested > account_balance:
    res=f"Hello {customer_name},Transaction failed; Insufficient funds to withdraw {amount_requested}. Your balance is {account_balance}"
else:
    account_balance = account_balance-(amount_requested + trans)
    res=f"Hell0 {customer_name}, {amount_requested} withdrawn successfully. New balance: {account_balance} "

print(res)

# Q2
# A trainer entered marks for five subjects and needs help analyzing
# student performance. Create a program that stores the marks in a list,
# calculates the average, awards grade A for averages of 70 and above,
# grade B for averages of 50 to 69, and grade C for anything below 50.
# If any subject score is below 40, display a message showing the
# student must retake that subject.

marks=[20,60,30,80,100]

average=sum(marks)/len(marks)
print(average)

if average>=70:
    grade='A'
elif average<70 and average>=50:
    grade='B'
elif average<50 and average>=40:
    grade='C'
else:
    grade='Retake the Subject'

print(grade)

# Q3

# A supermarket manager needs help checking stock levels. Create a
# program that stores product names and quantities in a dictionary,
# identifies items that are completely out of stock, and also shows
# products with quantities below five units that need urgent restocking.

stock = {
    "Milk": 10,
    "Bread": 2,
    "Eggs": 0,
    "Sugar": 4,
    "Rice": 7,
    "Soap": 0
}

# Check each product and its quantity
for item, quantity in stock.items():
    if quantity == 0:
        print(f"{item} is completely out of stock")
    elif quantity < 5:
        print(f"{item} has only {quantity} units. Needs urgent restocking")
    else:
        print(f"{item} has {quantity} units. Sufficient stock")

# Q4  ****loop****
# A company wants to secure employee accounts. Create a login
# system that stores a username and password, allows only three
# attempts, locks the account after three failed attempts, and welcomes
# the user when the correct credentials are entered.



# GROUP 2

# Q1
# An electricity company charges customers based on usage. Create a
# billing system where the first 100 units are charged at KES 15 each,
# while any additional units are charged at KES 20 each. If the final bill
# exceeds KES 5000, add 5% tax before displaying the total.

units=input("Enter units used: ")
units=int(units)


if units<=100:
    charge=units*15
elif units>100:
    charge=(100*15)+((units-100)*20)


if charge>5000:
    charge=(0.05*charge)+charge
    bill=f"bill is KES {charge}"
else:
    bill=f"bill is KES {charge}"

print(bill)


# Q2
# A hospital needs a smart queue system. Create a program that stores
# patient name and age. Patients above 60 years and children below 5
# years should receive priority service, while all others join the normal
# queue.

name=input("Enter patient name: ")
age=int(input("Enter patient age: "))

if age>60 or age<5:
    res=f"Patient is {age} years old. Give priority service."
else:
    res=f"Patient is {age} years old. Join normal queue."

print(res)

# Q3
# An online store wants an automated checkout system. Create a
# program that stores purchased items in a list and calculates the total
# cost. If the amount is above KES 3000, apply a 10% discount. If the
# total is below KES 1000, add a delivery fee.


items = ["Shoes", "Bag", "Watch"]

total=int(input("Enter total cost of items: "))
delivery_fee=250

if total>3000:
    total=total-(0.1*total)
    cost=f"Total is above KES 3000. Cost after discount is KES {total}."
elif total<1000:
    total=total+delivery_fee
    cost=f"Total is below KES 1000. Cost with delivery fee included is KES {total}."
else:
    remaining=3000-total
    cost=f"Total is KES {total}. Spend KES {remaining} more to get a 10% discount."

print(cost)

# Q4
# A website wants users to create stronger passwords. Build a
# password checker that verifies password length, checks whether it
# contains numbers and special characters, then classifies it as Weak,
# Medium, or Strong.

password=input("Enter Password: ")


if len(password) <6 and not password.isalnum:
    print("Weak")
elif len(password) >=6 and len(password) <=10 and password.isalnum:
    print("Medium")
elif len(password) >10 and password.isalnum:
    print("Strong")
else:
    print("Weak")


# GROUP 3

# Q1
# A driver is preparing for a road trip. Create a program that stores the
# amount of fuel available and the distance to travel. If one litre covers
# 12 km, determine whether the fuel is enough for the journey or if the
# driver should refill first.

fuel_available=float(input("Enter amount of fuel available (litres): "))
distance=float(input("Enter the total distance to travel (km): "))

cover=distance/fuel_available

if cover<=12:
    val=f"Fuel is enough for the journey."
else:
    rem=(distance/12)-(distance/cover)
    val=f"Refill first. {rem:.2f} more litres of fuel needed."

print(val)

# Chatgpt:

# distance_covered = fuel_available * 12

# if distance_covered >= distance:
#     print("Fuel is enough for the journey.")
# else:
#     extra_fuel = (distance - distance_covered) / 12
#     print(f"Refill first. You need {extra_fuel:.2f} more litres of fuel.")

# Q2
# A company wants to automate payroll. Build a program that stores an
# employee’s basic salary, adds allowances, then deducts tax.
# Employees earning above KES 80,000 should pay 30% tax while the
# rest pay 20%. Display the final net salary.

basic_salary=float(input("Enter basic salary: "))
allowance=float(input("Enter allowance: "))
salary=basic_salary+allowance

if salary>80000:
    salary=salary-(0.3*salary)
    net_salary=f"final net salary is {salary:.2f}"
else:
    salary=salary-(0.2*salary)
    net_salary=f"final net salary is {salary:.2f}"

print(net_salary)

# Q3
# A weather station records daily temperatures. Create a system that
# warns people when temperatures are above 35 degrees, warns of
# cold weather when below 15 degrees, and shows normal conditions
# otherwise.

temp=input("Enter temperature: ")
temp=float(temp)

if temp>35:
    value=f"Hot weather, temperature is {temp:.1f} degrees."
elif temp<15:
    value=f"Cold weather, temperature is {temp:.1f} degrees."
else:
    value=f"Normal weather, temperature is {temp:.1f} degrees."

print(value)

# Q4
# A courier company wants package tracking. Create a system that
# checks whether a package is delayed, delivered, or still in transit.
# Delayed packages should notify customers, delivered packages
# should display a thank-you message, and packages in transit should
# show estimated arrival.

status = input("Enter package status (delayed, delivered, in transit): ").lower()

if status=="delayed":
    note="Notification to customer, your package has been delayed."
elif status=="delivered":
    note="Your package has been delivered successfully. Thank you for choosing our courier service!"
elif status == "in transit":
    arrival = input("Enter estimated arrival date/time: ")
    note=f"Your package is still in transit.Estimated arrival:{arrival}"
else:
    note="Invalid package status entered."

print(note)


# GROUP 4

# Q1
# A school wants to stop students with pending balances from sitting
# exams. Create a program that checks a student’s fee balance. If the
# balance is greater than zero, deny access to the exam card.
# Otherwise allow printing.

balance=input("Enter balance: ")
balance=float(balance)

if balance>0.00:
    res='Access to Exam Card Denied'
else:
    res='Printing Allowed'

print(res)

# Q2
# A parking company wants to automate entry control. Build a program
# that stores the total parking spaces and occupied spaces, then
# calculates available slots. If the lot is full, deny new entry.

total_spaces = (input("Enter total parking spaces: "))
total_spaces=int(total_spaces)
occupied_spaces = (input("Enter occupied spaces: "))
occupied_spaces=int(occupied_spaces)

available_spaces = total_spaces - occupied_spaces

if available_spaces > 0:
    available_spaces=available_spaces-1
    value=f"Entry allowed. {available_spaces} spaces available."
else:
    value=f"Entry denied. {available_spaces} spaces available ."

print(value)

# Q3
# A mobile network provider wants to warn customers when internet
# bundles are low. Build a program that checks remaining data in MB. If
# below 100MB, warn the user. If zero, block browsing.

bundles=input("Enter  internet bundles:")
bundles=int(bundles)

if bundles == 0:
    val=f"Browsing blocked"
elif bundles < 100:
    val=f"Your {bundles}MB is below 100MB"
else:
    val=f"You have {bundles}MB"

print(val)

# Q4
# A retail shop wants to identify wholesale customers. Create a system
# that checks how many items a customer has bought. If items are more
# than five, reward points should be given.

items_bought = input('Enter Number of Items: ')
items_bought=int(items_bought)
wholesale_threshold = 5

if items_bought > 5:
    reward_points = items_bought/wholesale_threshold
    res=f'You have bought {items_bought} items.'
    res=f'You have earn {reward_points} points.'
else:
    remaining=wholesale_threshold-items_bought
    res=f'You have bought {items_bought} items. Add {remaining} more items to earn points'

print(res)


# GROUP 5

# Q1
# A bank is reviewing loan applications. Create a program that checks
# salary and age. Applicants below 21 years should be rejected, while
# those above 21 with salaries above KES 50,000 should be approved.

age=int(input("Enter your age: "))
salary=int(input("Enter your salary: "))

if age<21:
    res=f"Loan application rejected, your age is {age} years. Must be 21 or above to qualify."
elif age>=21 and salary>50000:
    res=f"Loan application approved, your salary of KES {salary} and age of {age} years meets the loan application requirements."
else:
    res=f"Loan application rejected, your salary of KES {salary} is below the minimum requirement of KES 50,000."

print(res)

# Q2
# A smartphone company wants a battery safety alert. Build a program
# that checks battery percentage. If below 20%, warn the user to
# charge. If below 5%, activate emergency mode.

battery_percentage=int(input("Enter battery percentage(%): "))

if battery_percentage<20 and battery_percentage>=5:
    disp=f"Low battery:{battery_percentage}%. Charge device."
elif battery_percentage<5:
    disp=f"Battery is at {battery_percentage}%. Emergency mode activated"
else:
    disp=f"Battery is at {battery_percentage}%. Sufficient power."

print(disp)

# Q3
# A school wants to monitor attendance. Create a system that stores
# attended classes and total classes, calculates attendance percentage,
# and warns students whose attendance is below 75%.

total_classes=int(input("Enter total classes: "))
attended_classes=int(input("Enter attended classes: "))

attendance_percentage=(attended_classes/total_classes)*100

if attendance_percentage<75:
    res=f"Attendance is {attendance_percentage}%. Needs improvement."
else:
    res=f"Attendance is {attendance_percentage}%. Keep it up."
    
print(res)

# Q4
# A courier company wants to improve communication. Build a system
# that compares expected delivery date with the current day and alerts
# customers if the package is delayed.

expected_day = int(input("Enter expected delivery day: "))
current_day = int(input("Enter current day: "))

if current_day > expected_day:
    ps="Alert to customer. Your package is delayed."

else:
    ps="Your package is on schedule."

print(ps)

# GROUP 6

# Q1
# A mobile money service needs a transfer checker. Create a program
# that stores account balance and transfer amount. If the balance is
# enough, process the transfer and deduct charges. Otherwise reject
# the transaction.
# Q2
# A water company charges penalties for heavy users. Build a billing
# program where customers using more than 50 units pay extra
# charges.
# Q3
# An online course platform wants to issue certificates automatically.
# Create a system that compares completed lessons with total lessons
# and awards a certificate once all lessons are complete.
# Q4
# A cybersecurity company wants suspicious logins detected. Build a
# program that stores a normal login country and compares it with the
# current login country. If different, request extra verification.

# GROUP 7

# Q1
# A payroll company needs to calculate employee taxes using different
# salary bands. Create a system that applies different tax rates
# depending on salary level and displays final pay.
# Q2
# A university hostel manager wants to know whether rooms are
# available. Create a program that checks room count and rejects new
# applicants when no rooms remain.
# Q3
# An investor watches stock prices daily. Build a program that sends
# alerts whenever a stock price drops below a chosen buying target.
# Q4
# A ride-hailing company wants to manage customer expectations. If no
# drivers are available nearby, inform the customer to retry later.

# GROUP 8

# Q1
# A registration portal must verify emails. Create a program that checks
# whether an email contains both @ and .com before accepting it.
# Q2
# A cinema only allows adults into some movies. Build a system that
# checks age and denies entry to anyone below 18 years.
# Q3
# A library wants automatic fines. Create a program that charges KES
# 20 per late day after seven allowed days.
# Q4
# A social media platform verifies popular users. Build a program that
# grants verification once followers exceed 10,000.

# GROUP 9

# Q1
# A fuel station wants to reward customers based on how much fuel
# they buy. Create a system that checks the number of litres purchased
# and applies a reward message only when the purchase exceeds a
# certain threshold.
# Q2
# An internet provider is monitoring user experience. Build a program
# that evaluates network speed readings and classifies them into poor,
# good, or excellent performance based on the value entered.
# Q3
# A restaurant needs a simple bill splitter. Create a system that takes a
# total bill amount and number of people, then determines how much
# each person should pay, including a check for invalid inputs.
# Q4
# A company is reviewing job applicants. Create a program that checks
# if an applicant meets minimum requirements such as experience and
# qualifications before shortlisting them.

# GROUP 10

# Q1
# An airline is pricing tickets differently for children and adults. Build a
# program that determines ticket cost based on age and applies a
# discount where applicable.
# Q2
# A warehouse is tracking stock levels. Create a system that monitors
# inventory and alerts when stock falls below a required minimum level
# for restocking.
# Q3
# A mobile money service has daily transaction limits. Build a program
# that checks if a transaction exceeds the allowed limit and rejects or
# approves it accordingly.
# Q4
# A laptop seller wants to verify warranty validity. Create a system that
# checks purchase year against the current year and determines
# whether warranty is still active.

# GROUP 11

# Q1
# A school administration system is tracking unpaid fees. Build a
# program that checks student payment status and flags those with
# outstanding balances.
# Q2
# A traffic system is monitoring speeding vehicles. Create a program
# that evaluates speed readings and determines whether a driver should
# be fined.
# Q3
# A website login system is being improved. Create a program that
# checks login credentials and determines whether a user should be
# granted full access, limited access, or denied entry.

# GROUP 12

# Q1
# An electricity token system is running low on units. Build a program
# that checks remaining token balance and warns users when they are
# close to exhaustion.
# Q2
# A library system is managing membership cards. Create a program
# that checks whether a membership card is expired and prevents
# borrowing if it is not valid.
# Q3
# A hospital appointment system is managing bookings. Build a program
# that checks doctor availability and either confirms an appointment or
# suggests an alternative date.
