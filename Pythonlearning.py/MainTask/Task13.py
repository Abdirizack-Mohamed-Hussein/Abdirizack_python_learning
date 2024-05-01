# TASK 13: Using Python 
# Write a program that takes the email and password as input from a user 
# and checks if they are equal to “admin@mail.com” and password is “Admin@123” , 
# if so then print  “Login is Successful” and if not print “Invalid username or password”. 
# ONLY accept 3 tries after which it notifies you that you have been blocked.

# Set the correct email and password
correct_email = "admin@mail.com"
correct_password = "Admin@123"

# variables for attempts
max_attempts = 3
attempts = 0

# Allow the user 3 attempts
for i in range(max_attempts):
    # Get email and password from the user
    user_email = input("Enter your email: ")
    user_password = input("Enter your password: ")

    # Check if the credentials are correct
    if user_email == correct_email and user_password == correct_password:
        print("Login is Successful")
        break  # Exit the loop if login is successful
    else:
        print("Invalid username or password")
        attempts += 1

# Check if the user has been blocked
if attempts == max_attempts:
    print("You have been blocked. Too many incorrect attempts.")
