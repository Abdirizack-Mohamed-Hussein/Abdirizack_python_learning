
# TASK 4: Using Python ...write this code inside a function.
# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.


# email = input("Enter your email address: ")  # Prompting the user for input
# def validate_email():

#     for i in range(0,len(email)):
#      if email.count("@")==1 and email.count(".")>=1:
#         if email[i]=="@":
#             at= i
#             print(at)
#         elif email[i]==".":
#             dot=i
#             print(dot) 
#     else:
#         print("invalid email")
# at = email.find("@")
# dot = email.find(".")

# if at < dot and at>1  and dot >at+1 and dot<len(email)-1:
#     print("valid email")
# else:
#     print("invalid email")

# at = email.find("@")
# dot = email.find(".")

# if email.count("@") == 1 and email.count(".") >= 1:
#     if at < dot and at > 1 and dot > at+1 and dot < len(email)-1:
#         print("valid email")
#     else:
#         print("invalid email")
# else:
#     print("invalid email")


# # # Calling the function to execute the code
# # validate_email()