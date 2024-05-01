age=int(input("Enter Your Age: "))
if(age<=0):
    print("Please Enter Your Valid Age")
else:
    if(age<13):
        print("Haha! You are still a Child!")
    elif(age>=13 and age<18):
        print("Aaaaw! You are a Teenager!")
    else:
        print("Oooh! You are an Adult! What are you doing in this World!")


  #IF-ELIF-ELSE
#  #Take a users input on points
# #write a program that checks on the grade based on the following conditions
        # 80-100=A
        # 70-79=B
        # 60-69=C
        # 50-59=D
        # 0-49=E
        # otherwise "invalid"             
Marks=float(input("Enter your Marks: "))
if (Marks>=0) and (Marks<=100):

   if (Marks>=90) and (Marks<=100):
     Grade=("A")
   elif (Marks>=80) and (Marks<=90):
    Grade=("B")
   elif (Marks>=70) and (Marks<=80):
    Grade=("C")
   elif (Marks>=60) and (Marks<=70):
    Grade=("D")
   elif (Marks>=50) and (Marks<=60):
    Grade=("E")
   else:
    Grade="Fail"
    
else:
    Grade=("invalid Grade")

# print(Grade)