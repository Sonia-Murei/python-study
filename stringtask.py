# Clean up the following variable to give the clean version in lower case.
name=" JOHn "
print(name.lower().strip())

# only display “Breed is German”
sentence_one = "The Dog Breed is German Shepherd"
print(sentence_one[8:23])

# only display “Clinton forces”
sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[16:30]) 

# Split the below sentence using a semicolon i.e ; And display length of the result.
print(len("The lazy dog; ran so fast; it hit the wall.".split(";")))

# Clean up and display Full name i.e John Doe
first_name = " Joh.n "
last_name = " Do,e "
name1= first_name.strip().replace(".","")
name2= last_name.strip().replace(",","")
print(name1+" "+name2)

# Having the string r = '["E","W","C"]' Manipulate it to display EWC
r= '["E","W","C"]'
r1= r.replace(",", "").replace("[", "").replace("]", "").replace('"', "")
print(r1)
