def password_checker():
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