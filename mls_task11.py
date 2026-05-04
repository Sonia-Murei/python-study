# Write a program that takes the date of birth of a person 
# and the program outputs the age in terms of years,months,days TODAY.datetime
# Once you learn functions,revisit this and write this code inside a function.

from datetime import date
import calendar

year = int(input("Enter birth year: "))
month = int(input("Enter birth month: "))
day = int(input("Enter birth day: "))

dob = date(year, month, day)
today = date.today()

years = today.year - dob.year
months = today.month - dob.month
days = today.day - dob.day

if days < 0:
    months -= 1
    prev_month = today.month - 1 or 12
    prev_year = today.year if today.month != 1 else today.year - 1
    days += calendar.monthrange(prev_year, prev_month)[1]

if months < 0:
    years -= 1
    months += 12

print("Age:", years, "years,", months, "months,", days, "days")
