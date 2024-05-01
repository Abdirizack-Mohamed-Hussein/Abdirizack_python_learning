
# TASK 5: Using Python ..write with a function
# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. 
# Return the largest of the three. 
# Do this without using the the inbuilt max () function!

# Prompting the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

def find_largest(a, b, c):
    largest = a  # Assume the first number is the largest initially
    
    # Compare with the second number
    if b > largest:
        largest = b
    
    # Compare with the third number
    if c > largest:
        largest = c
    
    return largest

# Calling the function to find the largest number
result = find_largest(num1, num2, num3)
print("The largest number is:", result)