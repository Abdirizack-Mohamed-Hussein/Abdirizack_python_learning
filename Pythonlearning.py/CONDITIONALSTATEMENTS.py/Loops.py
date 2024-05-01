#numbers btw 0 and 1000 in a list
numbers=list(range(0,1000))
print(numbers)

#syntax for for loop
for i in numbers:
 if(i%2==0):
    print(i)
#numbers btw 1000 and 2000 in a list
#display numbers divisible by 7 
    
    
Sevens=list(range(1000,2000))
  
for i in Sevens:
      if(i%7==0):
        print(i)

#SAVE numbers btw 1000 and 2000 in a list
#AND divisible numbers  by 7 
        
divisible_by_7=[]
Sevens=list(range(1000,2000))
  
for i in Sevens:
      if(i%7==0):
        divisible_by_7.append(i)
print(divisible_by_7)

#TASK
#SAVE numbers that are only divisible by 5 and 7 btw 0-500 in a LIST!
Fives_and_Sevens=list(range(0,500))
Fives_Sevens=[]

for i in Fives_and_Sevens:
 if(i%5==0 and i%7==0):
   Fives_Sevens.append(i)
print(Fives_Sevens)

fruits=["apple","banana","cherry","oranges"]    

for fruits in fruits:
    if("banana" in fruits):
      print("Available!")

sum=0
for num in range(1,101):
   sum+=num
print(sum)
   
   # TASK: Loops
# # Write a program that displays a numbers 1 to 50 inside a list.
a=list(range(1,51))
print(a)

# # From 1 above display the ones divisible by 7 or 5 inside a list.
b=[]
for a in range(1,50):
 if(a%5==0 or a%7==0):
   b.append(b)
   print(b)
 
# # # Find sum and average of values in the range between 10 to 40.

sum=0
average=[]
for i in range(10,41):
    sum+=i
    
    average.append(i)
    avg=sum/len(average)
print(sum)
print(avg)
#median
#mode
# # Put in a list the first 10 odd numbers between 10 to 50. 

list=[]
for num in range(10,51):
    if num%2!=0:
        list.append(num)

list1=list[0:10]
print(list1)

# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
num3=list(range(1,11))
number=float(input("Enter a number: "))
for i in num3:
   mult=i*number
   print(mult)

# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
Even_numbers=list(range[1,51])
Even=[]
for i in Even_numbers:
   if i%2==0:
      Even.append(i)
      Eve=Even[0:10]
    
print(Eve)
