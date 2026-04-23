if 50>30:
    print('50 is greater')

# Check is someone is eligible to vote
age=26

if age>18:
    print('Eligible to vote')
else:
    print('Not Eligible to vote')

# Check if temperature is greater than 30 print too hot otherwise normal temperature
temperature=26

if temperature>30:
    print('too hot')
else:
    print('normal temperature')

# Check if temperature is greater than 30 print too hot,
# if temperature is above 15 and less than 30 print normal temperature otherwise normal temperature

temp=7

if temp>30:
    print('too hot')
elif temp>15 and temp<30:
    print('normal temperature')
else:
    print('too low')

results=35

if results>80:
    print('Grade A')
elif results>70 and results<80:
    print('Grade B')
elif results>60 and results<70:
    print('Grade C')
elif results>50 and results<60:
    print('Grade D')
else:
    print('Grade E')