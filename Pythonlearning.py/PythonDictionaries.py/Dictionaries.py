# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # # Dictionaries are used to store data values in key:value pairs.
# # # Dictionaries are written with curly brackets, and have keys and values:
# person = {
#     "name":"John Doe", 
#     "age":30, 
#     "location": "Nairobi", 
#     "email" :"johndoe@mail.com"
#     }
# # # #access values use keys
# print(person["name"])
# print(person["age"])
# print(person["location"])
# print(person["email"])
# print(person)
# # # #adding key value pairs
# person["city"]="New york"
# print(person)

# person["polling station"]="moyale"
# print(person)

# person["occupation"]="programmer"
# print(person)

# # # #modify/update to nairobi
# person["age"]=40
# print(person)

# person["city"]="machakos"
# print(person)

# # # #display all keys
# print(person.keys())
# print(person.values())
# print(person.items())

# # # #TASK
# my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]
# # # #1. Print KES
# print(my_ds[3][2]["currency"])


# # # #TASKS
# my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]
# # # # 1. Print KES
# print(my_ds[3][2]["currency"])

# # # # 2. Print 560
# print(my_ds[2])

# # # # 3. Print Maths
# print(my_ds[3][1])

# # # 4. In the dictionary with the key currency, add another key “amount” with value 90
# # #UPDATE
# my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]
# my_ds[3][2]["amount"]=90
# print(my_ds)

# 5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
#      Hint: Strings can be reversed using [::]
my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]
my_ds[4]=str(my_ds[4])
my_ds[4]=my_ds[4][::-1]
# print(my_ds[4]).... change to integer
my_ds[4]=int(my_ds[4])
print(my_ds)


# # 6. Change the name “John” to “Jane” . 
# my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]
# my_ds[5]=list(my_ds[5])
# my_ds[5][1]="Jane"
# my_ds[5]=tuple(my_ds[5])
# print(my_ds)