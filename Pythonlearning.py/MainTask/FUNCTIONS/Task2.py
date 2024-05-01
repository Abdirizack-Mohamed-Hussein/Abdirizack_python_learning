# TASK 2: Using Python ....write this code inside a function
# Prompt the user for a number either on a form input or the terminal.
# Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?


num=int(input("Enter a number: "))  # Prompting the user for input
n=int(input("Enter a number: "))
def number():
    # Checking if the number is even or odd
    if num%2==0:
        print("Even_Number!")
    else:
        print("Odd Number!")  

number() # Calling the function to execute the code
    

# Extras:
# If the number is a multiple of 4, print out “divisible by 4”.

def divisible():
    if num%4==0:
        print("Divisible by 4!")
    else:
        print("Not divisible by 4!")
divisible()