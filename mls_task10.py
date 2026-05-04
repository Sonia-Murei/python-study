# Write a program that calculates the total stock in a company from the array/list below 
# if we know that the stock is the last digit in every array/list.

# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.
# Once you learn functions,revisit this and write this code inside a function.

prods = [['omo','30kshs','300'], ['milk','50kshs','200'],
         ['bread','45kshs','359'], ['coffee','5kshs','79']]

total = 0

for item in prods:
    total = total + int(item[-1])

print("Total stock:", total)

# Note:
# item[-1] picks the last value in each list (the stock)
# int() converts it from string to number
# Add everything into total
