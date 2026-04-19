days_of_the_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
print(type(days_of_the_week))
print(days_of_the_week[1])
print(days_of_the_week[2:4])

# display saturday from the tuple
print(days_of_the_week[6])

# display thirsday to saturday from the tuple
print(days_of_the_week[4:7])

# display Monday and Thursday from the tuple
print(days_of_the_week[1:5:3])

# convert tuple to list list(days_of_the_week)
days_of_the_week= list(days_of_the_week)
print(type(days_of_the_week))

# modify
days_of_the_week[2] = "Tue"

# convert list to tuple tuple(days_of_the_week)
days_of_the_week = tuple(days_of_the_week)
print(type(days_of_the_week))
print(days_of_the_week)

# convert sunday to sun from the tuple
days_of_the_week = list(days_of_the_week)
days_of_the_week[0] = "Sun"
days_of_the_week = tuple(days_of_the_week)
print(days_of_the_week)

# add january to the tuple
days_of_the_week = list(days_of_the_week)
days_of_the_week.append("January")  
days_of_the_week = tuple(days_of_the_week)
print(days_of_the_week)