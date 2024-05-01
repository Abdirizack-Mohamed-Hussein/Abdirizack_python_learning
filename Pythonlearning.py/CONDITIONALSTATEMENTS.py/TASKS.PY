# # # # # #write a program that checks if a number is a prime number

# # # # # number=int(input("Enter any positive number: "))

# # # # # if (number>1):
# # # # #      for i in range(2,number):
# # # # #         if (number%i)==0:
# # # # #          break
# # # # #          print("number,is not a prime number") 
# # # # #          # Numbers less than or equal to 1 are not prime.
# # # # #      else:
# # # # #       print("number,is a prime number")
# # # # # else:
# # # # #      print("number,is not a prime number") 

# #TASK
# # Take three inputs from a user, separately. Print the largest of the numbers.
# # Hint: Determine what type of data is taken in as input
a=float(input("Enter any number a: "))
b=float(input("Enter any number b: "))
c=float(input("Enter any number c: "))
if(a>b and b>c):
   print(a,"largest number")  #print(f"{a}largest number")
elif(b>a) and (b>c):              
   print(b,"largest number")  #print(f"{b}largest number")
elif(c>a) and (c>b):
   print(c,"largest number")  #print(f"{c}largest number")
else:
   print("try again")


# # Take as input from a user the temperature if the temperature is above 30°C display 
# # “The temperature is too high”,
# # otherwise display “Normal temperature”
   
temp=float(input("Enter your temperature: "))
if(temp>30):
   value="The temperature is too high!"
elif(temp>=15 and temp<=30):
   value="Normal temperature!"
elif(temp>=0 and temp<15):
   value="Low temperature!"
else:
   value="Extremely Cold!"
print(value)

#TASK
age=int(input("Enter your age: "))
if(age>=18):
    print(age,"eligible for voting")
else:
     print(age,"Not eligible for voting!")


# # #TASKS 3
# # 2.Write a program that asks the user to input two numbers
# # checks if  both numbers are  are positive and 
# # then checks if the sum of the numbers is even or odd.otherwise  print "negative numbers."
     
num1=float(input("Enter any number: "))
num2=float(input("Enter any number: "))

if(num1>=0 and num2>=0):
     print("Is a positive Number!")

     sum=num1+num2
     if(sum% 2==0):
      print("Even!")

     else:#(num1 +num2% 2==1)
      print("Odd!")

else:
    print("Is a Negative Number!")
    


 
# #TASK 1
# create  a file called nested_task.py then do the following
# 1.Write a program that takes a student's score input checks if the scores are between 0 and 100 and prints their grade (A, B, C, D, or F) based on the following conditions:
# A: 90 and above
# B: 80 - 89
# C: 70 - 79
# D: 60 - 69
# F: below 60
# otherwise prints invalid score 
    
score =float(input("Enter your Marks: "))
if (score >=0) and (score <=100):
 
 if (score >=90):
     Grade=("A")
 elif (score >=80) and (score <=89):
    Grade=("B")
 elif (score >=70) and (score <=79):
    Grade=("C")
 elif (score >=60) and (score <=69):
    Grade=("D")
 elif (score <60):
    Grade=("F")
 else:
    Grade="Invalid Score!"
    
    
else:
 Grade=("invalid Grade")

print(Grade)


#TASKS
# 3.write a program that takes the user's input for a time in 24-hour format 
#converts it to 12-hour format.
# Consider handling cases for noon and midnight appropriately.


