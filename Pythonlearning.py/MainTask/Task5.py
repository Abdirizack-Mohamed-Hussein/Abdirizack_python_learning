# TASK 5: Using Python 
# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. 
# Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
c = float(input("Enter the third number (c): "))

if a >b and a >c:
   print(f"The largest number among {a}, {b}, and {c} is: {a}")

if b > c  and b>a :
    print(f"The largest number among {a}, {b}, and {c} is: {b}")
  

if c >a and c > b :
    print(f"The largest number among {a}, {b}, and {c} is: {c}")