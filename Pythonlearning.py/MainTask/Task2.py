# TASK 2: Using Python 
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd,
#  display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
Number=float(input("Enter a number: "))

if (Number % 2==0):
    print("Even")
    if (Number%4==0):

        print("divisible by 4")

else:
 print("Odd")
# 
#  Extras:
# If the number is a multiple of 4, print out “divisible by 4”.
 
#  Number=float(input("Enter a number: "))



