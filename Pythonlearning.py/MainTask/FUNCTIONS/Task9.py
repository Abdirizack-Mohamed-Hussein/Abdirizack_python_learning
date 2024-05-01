# TASK 9: Using Python ...write this code inside a function.
# Write a program called stars. It should prompt the user for a number, 
# and it should print the number of stars till the number entered.


num = int(input("Enter a number: "))

def print_stars():
   
    if num:
        for i in range(1, num + 1):
            print("*" * i)
    else:
        print("Please enter a valid integer.")

# Calling the function to execute the code
print_stars()

