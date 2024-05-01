# TASK 13: Using Python .... write this code inside a function.
# Write a program that takes the email and password as input from a user 
# and checks if they are equal to “admin@mail.com” and password is “Admin@123” , 
# if so then print  “Login is Successful” and if not print “Invalid username or password”. 
# ONLY accept 3 tries after which it notifies you that you have been blocked.


email = input("Enter your email: ")
password = input("Enter your password: ")
attempts = 3
remaining=[]
def login_check():
    correct_email = "admin@mail.com"
    correct_password = "Admin@123"

    for i in range(attempts):
        if email == correct_email and password == correct_password:
            print("Login is Successful.")
            return
        else:
            remaining=attempts-1
            print("Invalid username or password.")
            
    print("You have been blocked.")

# Calling the function to execute the code
login_check()
