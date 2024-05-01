
# Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
name ="  JOHn  ." #to "john"
name="JOHn.".strip()
print(name)

#lower case....string.lower()
name="JOHn.".lower()
print(name)

#upper case...string.upper()
name="JOHn.".upper()
print(name)

# Slice the below string to get you the resulting sentence:
sentence_one = "The Dog Breed is German Shepherd"   
# only display "Breed is German"
sentence_one[8:]
print(sentence_one[8:-9])
print(sentence_one[8:23])   #last index plus 1 

sentence_two = "Defeats for the Clinton forces, this was her moment of triumph" 
# only display "Clinton forces"
sentence_two =sentence_two[16:31]
print(sentence_two[16:30])
print(sentence_two[16:-32])

# Split the below sentence using a semicolon i.e ; And display length of the result. 
dog="The lazy dog; ran so fast; it hit the wall."
dog.split(";")
print(dog)
print(len(dog))

first_name="  Joh.n"  
last_name="   Do,e"  #Clean up and display Full name i.e John Doe
first_name="Joh.n".strip().replace(".","")
last_name="Do,e".strip().replace(",","")
print(first_name)
print(last_name)
x= first_name + " " + last_name
print(x)

# Having the string r = '["E","W","C"]' #Manipulate it to display EWC

r = '["E","W","C"]'
r="".join(filter(str.isalpha,r))
print(r)
