# TASK 1: Using Python ...write this code inside a function.
# Write a program that prompts the user to enter the base and height of a triangle and returns its area.


base=float(input(" Enter the base: "))  # Prompting the user for input
height=float(input(" Enter the height: "))
def triangle(a,b):
    Area=0.5*a*b
    return Area

Area_triangle=triangle(base,height) # Calling the function to execute the code
print(Area_triangle)