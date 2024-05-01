# TASK 3: Using Python 
# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking 
# if it starts with +254.. or 07.. or 71… or 254.. or 01... Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”
Phone_number=input("Enter your Phone Number: ")

if Phone_number[0:4]=="+254 "and len(Phone_number==13):
    print(Phone_number)

elif Phone_number[0:2]=="07" and len(Phone_number)==10:

    print("+254"+ Phone_number[1:])
elif Phone_number[0:2]=="01" and len(Phone_number)==10:
    print("+254"+ Phone_number[1:])
elif Phone_number[0:2]=="71" and len(Phone_number)==9:

    print("+254"+ Phone_number[0:])
elif Phone_number[0:3]=="254" and len(Phone_number)==12:

    print("+"+ Phone_number)
else:
    print("Invalid Number!")

   