# TASK 12: Using Python 
# Write a program that prints the largest of 4 inputs taken in from a user. 
# Assume that the user would not enter any two numbers which are the same.

# a variable to store the largest number
largest_number = 0

# Get four numbers from the user
for i in range(4):
    user_input = float(input(f"Enter number {i + 1}: "))
    
    # Check if the current input is larger than the current largest number
    if user_input > largest_number:
        largest_number = user_input

# Display the largest number
print(f"The largest number is: {largest_number}")
