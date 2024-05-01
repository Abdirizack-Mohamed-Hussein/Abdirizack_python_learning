# TASK 9: Using Python 
# Write a program called stars. It should prompt the user for a number, 
# and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:

# Taking input for the number of rows
rows = int(input("Enter the number of rows: "))

# Printing stars based on the input
for i in range(1, rows + 1):
    print("*" * i)
