my_dict = {
    "name": "Jane",
    "gender": "Female",
    "age": 23,
    "city": "Nairobi"
}
print(my_dict)
print(type(my_dict))

#  Accessing values in a dictionary using keys
print(my_dict["name"])
print(my_dict["age"])

# Updating values in a dictionary
my_dict["age"] = 24
my_dict["city"] = "Mombasa"
print(my_dict)

# Adding new key-value pairs to a dictionary
my_dict["country"] = "Kenya"
my_dict["occupation"] = "Data Scientist"
print(my_dict)

my_dict["hobbies"] = ["Reading", "Traveling", "Cooking"]
print(my_dict["hobbies"][1])

# Dictionary methods
my_dict.pop("age")
print(my_dict)

my_dict.popitem()
print(my_dict)