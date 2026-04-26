# Q1
# A school wants to stop students with pending balances from sitting
# exams. Create a program that checks a student’s fee balance. If the
# balance is greater than zero, deny access to the exam card.
# Otherwise allow printing.

balance=input("Enter balance: ")
balance=float(balance)

if balance>0.00:
    print('Access Denied')
else:
    print('Access Granted')

# Q2
# A parking company wants to automate entry control. Build a program
# that stores the total parking spaces and occupied spaces, then
# calculates available slots. If the lot is full, deny new entry.
    # You need to:
        # Store total parking spaces
        # Store currently occupied spaces
        # Calculate available spaces
        # Decide whether to allow entry

total_spaces = (input("Enter total parking spaces: "))
total_spaces=int(total_spaces)
occupied_spaces = (input("Enter occupied spaces: "))
occupied_spaces=int(occupied_spaces)

available_spaces = total_spaces - occupied_spaces

if available_spaces > 0:
    print("Entry allowed.")
else:
    print("Parking full. Entry denied.")

# Q3
# A mobile network provider wants to warn customers when internet
# bundles are low. Build a program that checks remaining data in MB. If
# below 100MB, warn the user. If zero, block browsing.

bundles=input("Enter  internet bundles:")
bundles=int(bundles)

if bundles == 0:
    print("Browsing blocked")
elif bundles < 100:
    print("Warning! Low internet bundles")
else:
    print("Sufficient internet bundles")

    # Theuri's Answer

# data=input('Enter Remaining Data: ')
# data=float(data)

# if data > 0 and data <= 100:
#     print('Your Data is below 100MB')
# elif data >= 100:
#     print('Your Data is enough')
# else:
#     print('Buy data')

# Q4
# A retail shop wants to identify wholesale customers. Create a system
# that checks how many items a customer has bought. If items are more
# than five, reward points should be given.

    # Arik's Answer

# items_bought = input('Enter Number of Item: ')
# items_bought=int(items_bought)
# wholesale_threshold = 5
# Reward_points = 10

# if items_bought > 5:
#     reward_points = 10
#     print(f'You have bought {items_bought} items.')
#     print(f'You have earn {Reward_points} points.')
# else:
#     print(f'You have bought {items_bought}items. buy more than 5 to earn points')

item_number=input("Enter number of items bought: ")
item_number=int(item_number)

if item_number>5:
    print("Give reward points")
else:
    print("No reward points")
