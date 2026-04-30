# Write a program that displays a numbers 1 to 50 inside a list.

lst=list(range(1,51))
print(lst)

# From 1 above display the ones divisible by 7 or 5 inside a list.

divisible_num=[]

for y in lst:
    if y%5==0 or y%7==0:
        divisible_num.append(y)
        
        
print(divisible_num)


# Find sum and average of values in the range between 10 to 40.

list1=list(range(10,41))

total = sum(list1)
average = total / len(list1)

print("Sum =", total)
print("Average =", average)

# Put in a list the first 10 odd numbers between 10 to 50. 

list2=list(range(10,51))
odd_numbers=[]

for o in list2:
    if o%2 != 0:
        odd_numbers.append(o)
    if len(odd_numbers) == 10:
        break

print(odd_numbers)

# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
    
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop

count = 0

for i in range(1, 51):
    if i % 2 == 0:
        count = count + 1

print("Total even numbers:", count)

# ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
# Display the total quantity of the 3 above.

ls1 = [("Jay", 20), ("Mo", 30), ("Mya", 32)]

total = 0

for item in ls1:
    total =total + item[1]

print("Total quantity:", total)
