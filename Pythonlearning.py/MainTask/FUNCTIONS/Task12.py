# TASK 12: Using Python ...write this code inside a function.
# Write a program that prints the largest of 4 inputs taken in from a user. 
# Assume that the user would not enter any two numbers which are the same.

# Prompting the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

def find_largest(num1, num2, num3, num4):
    largest = num1

    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    if num4 > largest:
        largest = num4

    print("The largest number is:", largest)

# Calling the function to find the largest number
find_largest(num1, num2, num3, num4)
