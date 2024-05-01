#prime number
x=0
num=int(input("Enter any Number: "))
if num==0 or num==1:
    x=1
    for i in range(2,num):
        if num%i==0:
            x=1
        if x==1:
         print("Entered number is not prime!")
    else:
         print("Entered number is prime!")


