#function called celsius_to_fahrenheit #parameter celsius #returns temp in fahrenheit
celsius=float(input("Enter the temp: "))

def celsius_to_fahrenheit(celsius):
    temp=(celsius*9/5)+32
    return temp
F=celsius_to_fahrenheit(celsius)
print(F)

#Reverse_string
string=input("Enter a string: ")
def reverse_string(string):
    text=string[::-1]
    return text
R=reverse_string(string)
print(R)


#function called square #parameter number #returns a square
number=float(input("Enter a number: "))
def square(number):
    Sq=number*number #number**2
    return Sq
S=square(number)
print(S)
