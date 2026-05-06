# TASK 15: 
# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary 
# then uses  the gross salary to find the NHIF. 

def calc_gross(basic,benefits):
    gross=basic+benefits
    return gross

basic_salary=float(input('Enter your basic salary: '))
benefits=float(input('Enter your benefits: '))

gross_salary=calc_gross(basic_salary,benefits)
print("Gross Salary:", gross_salary)

def nhif(contribution):
    if gross_salary<=5999:
        contribution=150
    elif gross_salary>=6000 and gross_salary<=7999:
        contribution=300
    elif gross_salary>=8000 and gross_salary<=11999:
        contribution=400
    elif gross_salary>=12000 and gross_salary<=14999:
        contribution=500
    elif gross_salary>=15000 and gross_salary<=19999:
        contribution=600
    elif gross_salary>=20000 and gross_salary<=24999:
        contribution=750
    elif gross_salary>=25000 and gross_salary<=29999:
        contribution=850
    elif gross_salary>=30000 and gross_salary<=34999:
        contribution=900
    elif gross_salary>=35000 and gross_salary<=39999:
        contribution=950
    elif gross_salary>=40000 and gross_salary<=44999:
        contribution=1000
    elif gross_salary>=45000 and gross_salary<=49999:
        contribution=1100
    elif gross_salary>=50000 and gross_salary<=59999:
        contribution=1200
    elif gross_salary>=60000 and gross_salary<=69999:
        contribution=1300
    elif gross_salary>=70000 and gross_salary<=79999:
        contribution=1400
    elif gross_salary>=80000 and gross_salary<=89999:
        contribution=1500
    elif gross_salary>=90000 and gross_salary<=99999:
        contribution=1600
    else:
        contribution=1700
    return contribution


# Calling
nhif_value=nhif(gross_salary)
print("NHIF:",nhif_value)

# TASK 16: 
# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate  using 6% of the Gross Salary. 
# BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF.

def nssf(gross_salary):
    if gross_salary < 18000:
        return 0
    else:
        return 0.06 * gross_salary
    

# Calling
nssf_value = nssf(gross_salary)
print("NSSF:", nssf_value)

# If nssf is capped at 18000:

# def nssf(gross_salary):
#    if gross_salary > 18000:
#        nssf_base = 18000
#    else:
#        nssf_base = gross_salary
    
#    nssf_rate = 0.06 * nssf_base
#    return nssf_rate

# print(nssf(gross_salary))

# Task 17: 
# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015

def nhdf(gross_salary):
    nhdf_rate=gross_salary *  0.015
    return nhdf_rate


# Calling
nhdf_value = nhdf(gross_salary)
print("NHDF:",nhdf_value)

# Task 18: 
# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 

def taxable_income(gross_salary,nhif,nssf,nhdf):
    taxable_inc=gross_salary - (nssf + nhdf + nhif) 
    return taxable_inc

taxable_inc = taxable_income(gross_salary, nhif_value, nssf_value, nhdf_value)

print("Taxable Income:",taxable_inc)


# NB:/
# Functions ≠ values i.e 
    # Functions are used to produce values
    # Values (results) are what you use in calculations
    # you must CALL a function to get a value before using it in calculations
# Always call the function to get the value before using it in calculations
# Example
    # def add(a, b):
    #     return a + b
    # add → function
    # add(2, 3) → value (5)

    # Therefore:

    # result = add(2, 3)   # calling the function → gives value 5
    # print(result)        # prints 5

# TASK 19: 
# Continue with the same program and find the person's PAYEE using the taxable income above.

def payee(taxable_income):
    if taxable_income<=24000:
        tax=0.1*taxable_income
    elif taxable_income<=32333:
        tax=0.1*24000+(0.25*(taxable_income-24000))
    elif taxable_income<=500000:
        tax=(0.1*24000)+(0.25*8333)+(0.3*(taxable_income-32333))
    elif taxable_income<=800000:
        tax=(0.1*24000)+(0.25*8333)+(0.3*467667)+(0.325*(taxable_income-500000))
    else:
        tax=(0.1*24000)+(0.25*8333)+(0.3*467667)+(0.325*300000)+(0.35*(taxable_income-800000))
    
    relief=2400
    final_tax=tax-relief
    return final_tax

# Calling 
payee_value = payee(taxable_inc)

print("PAYEE:", payee_value)

# NB:/
    # Using max() i.e max(final_tax,0), prevents negative tax because if someone earns a low salary, tax could be less than 2400
    # That gives a negative PAYEE

# Task 20: 
# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

def net_salary(gross_salary,nhif,nssf,nhdf,payee):
    net_salary=gross_salary-(nhif + nssf + nhdf + payee)
    return net_salary

# NB:/
# nhif, nssf, etc. are values passed into the function
# You must use these parameters, NOT outside variables e.g nhif_value, nssf_value etc.
    # i.e
            # net_salary(gross_salary, nhif_value, nssf_value, nhdf_value, payee_value)
        # You are sending values into the function

      # Inside the function:
            # def net_salary(gross_salary, nhif, nssf, nhdf, payee):
         # Those values are now renamed as parameters
         # You use them in calculations

net_salary_value= net_salary(gross_salary,nhif_value,nssf_value,nhdf_value,payee_value)
print("Net Salary:", net_salary_value)
