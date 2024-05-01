# TASK 6:Using Python or PHP 
# Write a program input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. 
# If the password is correct access is granted. After you show them a message , the account is blocked.

correct_password = "admin@123"
Attempts = 4

# while Attempts > 0:
for i in range(1,5):
    password = input("Enter the password: ")

    if password == correct_password:
        print("Access granted. Welcome!")
        break
    else:
        Attempts -=1
        if Attempts > 0:
            print(f"Incorrect password. {Attempts} Attempts remaining!")
        else:
            print("Incorrect password. Account is blocked.")




     