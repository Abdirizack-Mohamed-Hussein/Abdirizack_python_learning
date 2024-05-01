
# Conditional statements
# Conditional statements in Python are used for decision-making in code based on specific conditions. 
# The most commonly used conditional statements are:

# 1. if statement:
#    - Executes a block of code if a given condition is true.
a=5
b=10
if (a>b):
    print("a is greater")

# 2. if-else statement:
#    - Executes a block of code if the condition is true and another block if it is false.

#EXAMPLES

a=5
if (a>b):
    print("a is greater")

else:
    print("b is greater")

#Take a user's input for marks...(input function)
 #write a program that checks if marks is above 50
    #display pass
    #otherwise displays false
marks=int(input("Enter marks: "))
if (marks>=50):
        print("pass")
elif(marks>=40) and ((marks<50)):
        print("average")
else:
        print("fail")

# #ELIF
        # 3. if-elif-else statement:
#    - Used when multiple conditions need to be checked.
#         #IF-ELIF-ELSE
#  #Take a users input on points
# #write a program that checks on the grade based on the following conditions
        # 80-100=A
        # 70-79=B
        # 60-69=C
        # 50-59=D
        #0-49=E
        # otherwise "invalid"             
Points=float(input("Enter your Points?"))
if (Points>=80) and (Points<=100):
    print("A")
elif (Points>=70) and (Points<=79):
    print("B")
elif (Points>=60) and (Points<=69):
    print("C")
elif (Points>=50) and (Points<=59):
    print("D")
elif (Points>=0) and (Points<=49):
    print("E")      
else:
    print("invalid")


#Check if a  number is Even
number=float(input("Enter Number: "))
if(number % 2==0):
    print("Even")
else:
    print("odd")


    #WEIGHT CONVERTER

Weight=int(input("What is your Weight: "))
unit=input("(L)bs or (K)g: ")
if unit.upper()=="L":
    Converted=Weight*0.45
    print(f"Your are ({Converted} Kilos)")
else:
    Converted=Weight/0.45
    print(f"Your are {Converted} Pounds")

#     Nested If
# You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")





