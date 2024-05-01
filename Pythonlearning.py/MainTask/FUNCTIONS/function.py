# # def Hello():  #Defining functions
# #     print("Hello Abdirizack!")

# # #calling functions
# # Hello()

# #parameters and arguments= arguments are actual values 

# #Area of a rectangle
# def area_rectangle(l,w):
#     area=l*w
#     print(area)
# length=float(input("Enter the length: "))
# width=float(input("Enter the width: "))

# area_rectangle(length,width)

# #even or odd
# def num(x):
#     if x%2==0:
#         print("Even Number!")
#     else:
#         print("Odd Number!")
# number=int(input("Enter a number: "))
# num(number)

#TASK
# Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,
# then a functions that finds the grade according to the table below. 
# Use the value from total to get the average and average to find the grade.

# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

maths=float(input("Enter your maths: "))
eng=float(input("Enter your eng: "))
swa=float(input("Enter your swa: "))
sci=float(input("Enter your sci: "))
sos=float(input("Enter your sos: "))

def total_marks(a, b, c, d, e):

    total_marks=a+b+c+d+e
    return(total_marks)
total=total_marks(maths, eng, swa, sci, sos)
print(total)
def avg(a,b):
    avg=a/b
    return avg
num_subjects=5
score=avg(total,num_subjects)
print(score)


def Grade_marks(marks):

    if marks>79:
        Grade="A"
    elif marks>=60 and marks<=79:
          Grade="B"
    elif marks>=49 and marks<=59:
          Grade="C"
    elif marks>=40 and marks<=49:
          Grade="D"
    elif marks<40:
          Grade="E"
    else:
         Grade("Invalid marks")
    return Grade
total_grade=Grade_marks(score)
print(total_grade)