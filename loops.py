fruits=["mango","apple","banana"]

for p in fruits:
    print(p)

# Display even numbers between 10 and 100 in a list.

numbers=list(range(10,101))
even_numbers=[]

for x in numbers:
    if x%2==0:
        even_numbers.append(x)


print(even_numbers)

# Advanced loops method:
# for i in range(10, 101, 2):
# # print(i)

# Display numbers divisible by 3 and 7 between 1 and 100:

num=list(range(1,101))
divisible_num=[]

for y in num:
    if y%3==0 and y%7==0:
        divisible_num.append(y)
        
        
print(divisible_num)


tries=3
attempts=list(range(1,4))

tries=3
attempts=list(range(1,4))

for i in attempts:
	pin=input('Enter pin:')
	correct_pin='1234'
	if pin==correct_pin:
		print("Welcome")
		break
	else:
		remaining_tries=tries-i
		if remaining_tries>0:
			print(f'incorrect pin try again {remaining_tries} tries remaining')
		else:
			print("account Blocked")