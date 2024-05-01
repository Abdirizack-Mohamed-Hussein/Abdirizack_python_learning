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