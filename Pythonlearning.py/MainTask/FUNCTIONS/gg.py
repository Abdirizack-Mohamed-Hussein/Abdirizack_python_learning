def password_checker():
    # Defining the correct password
    correct_password = "admin@123"
    attempts = 4

    # Prompting the user for input
    password = input("Enter the password: ")

    # Checking if the password is correct
    if password == correct_password:
        print("Access granted.")
        return
    else:
        attempts -= 1
        print(f"Incorrect password. {attempts} attempts left.")

    # Prompting for password three more times
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted.")
        return
    else:
        attempts -= 1
        print(f"Incorrect password. {attempts} attempts left.")

    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted.")
        return
    else:
        attempts -= 1
        print(f"Incorrect password. {attempts} attempts left.")

    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted.")
    else:
        print("Account is blocked.")

# Calling the function to execute the code
password_checker()
