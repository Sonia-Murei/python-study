days_of_the_Week={"Mon", "Tue", "Wed","Mon", "Thu", "Fri", "Sat", "Sun","Sun"}
print(days_of_the_Week)

# Remove friday and sunday from the set using methods.
days_of_the_Week.remove("Fri")
days_of_the_Week.remove("Sun")
print(days_of_the_Week)

# Add them back to the set
days_of_the_Week.add("Fri")
days_of_the_Week.add("Sun")
print(days_of_the_Week)
