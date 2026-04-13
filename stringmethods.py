text="Software Developer"

# Capitalize is used to make the first letter of the string uppercase
text1=text.capitalize()
print(text1)

#  Count is used to count the number of appearances of a specific character 
text2=text.count("o")
print(text2)

# .upper() is used to make all the letters of the string uppercase
text3=text.upper()
print(text3)    

# .lower() is used to make all the letters of the string lowercase
text4=text.lower()
print(text4)    

text5=text.casefold()
print(text5)

# .find() is used to find the index of the first occurrence of a specific character. It returns -1 if the character is not found.
print(text.find("d"))

# .replace() is used to replace a specific character or substring with another character or substring.
print(text.replace("Developer","Engineer"))

# .index() is used to find the index of the first occurrence of a specific character. It raises a ValueError if the character is not found.
print(text.index("e"))

email="soniamurei@gmail.com"
split_email=email.split("@")
print(split_email)

text6=text.split()
print(text6)

# Quiz 1: Clean to Junior developer
text="    jUnIoR deVelOper     "

text=text.strip()
text=text.capitalize()
print(text)