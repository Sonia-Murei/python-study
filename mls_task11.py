# Write a program that takes the date of birth of a person 
# and the program outputs the age in terms of years,months,days TODAY.datetime
# Once you learn functions,revisit this and write this code inside a function.


from datetime import datetime

today=datetime.now()
print(today)
current_year=today.year
print (current_year)
current_month=today.month
print(current_month)
current_day=today.day
print(current_day)

dob=input('Enter date of birth(yyyy/mm/dd): ')

dob=dob.split('/')
print(dob)

birth_year=int(dob[0])
birth_month=int(dob[1])
birth_date=int(dob[2])

years=current_year-birth_year
months=current_month-birth_month
days=current_day-birth_date


# if days<0:
#     if months>0:
#         months=months-1
#         days=30+days
#     else:
#         years=years-1
#         months=12+months
#         days=30+days

if months<0:
    years=years-1
    months=12+months
    if days<0:
        months=months-1
        days=30+days
else:
    if months==0 and days<0:
        years=years-1
        months=12
        months=months-1
        days=30+days
    else:
        if days<0:
            months=months-1
            days=30+days

print(f"Years: {years}, month: {months}, days: {days}")

    # ChatGPT Answer 

# from datetime import date
# import calendar

# year = int(input("Enter birth year: "))
# month = int(input("Enter birth month: "))
# day = int(input("Enter birth day: "))

# dob = date(year, month, day)
# today = date.today()

# years = today.year - dob.year
# months = today.month - dob.month
# days = today.day - dob.day

# if days < 0:
#     months -= 1
#     prev_month = today.month - 1 or 12
#     prev_year = today.year if today.month != 1 else today.year - 1
#     days += calendar.monthrange(prev_year, prev_month)[1]

# if months < 0:
#     years -= 1
#     months += 12

# print("Age:", years, "years,", months, "months,", days, "days")