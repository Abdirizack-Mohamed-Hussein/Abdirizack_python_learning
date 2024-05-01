# TASK 1: Using Python ...write this code inside a function.
# Write a program that prompts the user to enter the base and height of a triangle and returns its area.


# base=float(input(" Enter the base: "))  # Prompting the user for input
# height=float(input(" Enter the height: "))
# def triangle(a,b):
#     Area=0.5*a*b
#     return Area

# # Area_triangle=triangle(base,height) # Calling the function to execute the code
# # print(Area_triangle)

# TASK 2: Using Python ....write this code inside a function
# Prompt the user for a number either on a form input or the terminal.
# Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?


# num=int(input("Enter a number: "))  # Prompting the user for input
# n=int(input("Enter a number: "))
# def number():
#     # Checking if the number is even or odd
#     if num%2==0:
#         print("Even_Number!")
#     else:
#         print("Odd Number!")  

# number() # Calling the function to execute the code

     

# Extras:
# If the number is a multiple of 4, print out “divisible by 4”.

# def divisible():
#     if num%4==0:
#         print("Divisible by 4!")
#     else:
#         print("Not divisible by 4!")
# divisible()

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

# # TASK 5: Using Python ..write with a function
# # Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. 
# # Return the largest of the three. 
# # Do this without using the the inbuilt max () function!

# # Prompting the user for input
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# def find_largest(a, b, c):
#     largest = a  # Assume the first number is the largest initially
    
#     # Compare with the second number
#     if b > largest:
#         largest = b
    
#     # Compare with the third number
#     if c > largest:
#         largest = c
    
#     return largest

# # Calling the function to find the largest number
# result = find_largest(num1, num2, num3)
# print("The largest number is:", result)

# TASK 6:Using Python ...write this code inside a function.
# Write a program input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. 
# If the password is correct access is granted. After you show them a message , the account is blocked.


def password_checker():
# Defining the correct password
    correct_password = "admin@123"
    attempts = 4

    for i in range(attempts):
        password = input("Enter the password: ")
        if password == correct_password:
            print("Access granted.")
            return
        else:
            attempts -= 1
            print(f"Incorrect password. {attempts} attempts left.")

    print("Account is blocked.")

# Calling the function to execute the code
password_checker()