# Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,
# then a functions that finds the grade according to the table below. 
# Use the value from total to get the average and average to find the grade.
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

def total_marks(maths,eng,swa,sci,sos):
    total=maths+eng+swa+sci+sos
    return total

def average_marks(total):
    average=total/5
    return average

def grade(average):
    if average>79:
        return 'A'
    elif average>=60 and average<=79:
        return 'B'
    elif average>=50 and average<=59:
        return 'C'
    elif average>=40 and average<=49:
        return 'D'
    else:
        return 'E'
    
maths=int(input("Enter marks for Maths: "))
eng=int(input("Enter marks for English: "))
swa=int(input("Enter marks for Swahili: "))
sci=int(input("Enter marks for Science: "))
sos=int(input("Enter marks for Social Studies: "))

total=total_marks(maths,eng,swa,sci,sos)
print(f'Total marks: {total}')

average=average_marks(total)
print(f'Average marks: {average}')

grade=grade(average)
print(f'Grade: {grade}')