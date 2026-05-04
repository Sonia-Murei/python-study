# Write a program that takes as input the speed of a car e.g 80. 
# If the speed is less than 70, it should print “Ok”. 
# Otherwise, for every 5 km/s above the speed limit (70), 
# it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. 
# If the driver gets more than 12 points, the function should print: “License suspended”.
# Once you learn functions,revisit this and write this code inside a function.

speed = int(input("Enter the speed: "))

if speed < 70:
    result = "Ok"
else:
    points = (speed - 70) // 5
    
    if points > 12:
        result = f"{points} points accumulated. License suspended"
    else:
        result = f"Points: {points}"

print(result)

# / → gives decimal (wrong here)
# // → gives whole number (correct for counting points)