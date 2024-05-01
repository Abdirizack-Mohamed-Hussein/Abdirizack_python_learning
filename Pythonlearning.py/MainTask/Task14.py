# TASK 14: Using Python
# Write a program that takes input of 2 values and adds them. The program should only accept numbers 
# and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .

# variables for input validation
valid_input = False    #Boolean 

# Loop until valid input is provided
for i in range(1,4):  # Allowing up to 3 attempts
    # Get input from the user
    input1 = input("Enter the first value: ")
    input2 = input("Enter the second value: ")

    # Check if both inputs are numeric or float
    if input1.isnumeric():
        if input2.isnumeric():
            # Convert inputs to float and perform addition
            result = float(input1) + float(input2)
            print(f"The sum is: {result}")
            valid_input = True #Boolean
            break
        else:
            print("Invalid character entered. Please enter numeric or float values.")
    else:
        print("Invalid character entered. Please enter numeric or float values.")

# Display an error if valid input is not provided after 3 attempts
if  valid_input>3:
    print("You have reached the maximum number of attempts. Exiting.")
