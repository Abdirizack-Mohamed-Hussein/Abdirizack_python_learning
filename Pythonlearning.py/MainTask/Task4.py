# TASK 4: Using Python 
# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.
Email=input("Enter your Email: ")

# if Email.count("@")==0  and Email.count(".")==0:
#    print(Email,"Correct Email")

# else:
#     print("Invalid Email!")


#CORRECT WAYl.com

for i in range(0,len(Email)):
    print(Email[i])