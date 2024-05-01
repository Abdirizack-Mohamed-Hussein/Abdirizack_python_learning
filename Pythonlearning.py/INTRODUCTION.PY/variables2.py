x=5
y="Hello, World!"
#python has no command for declaring a variable.
#In python, variables are created when you assign a value to it.


#VARIABLES are containers for storing data values.
#variables are created the moment you first assign a value to it.
x=5
y= "ABDIRIZACK!"
print(x)
print(y)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x=4       #x is of type int
x= "HABIBA!"    #x is now of type str
print(x)

#VARIABLES
#python allows one to assign values to multiple variables in one line.
x, y, z= "Orange", "Banana", "Cheery"
print(x)
print(y)
print(z)

#One value to Multiple variables
x=y=z="Orange"
print(x)
print(y)
print(z)

#UNPACK a collection
# #if you have a collection of values in a list , tuple. Python allows you to extract the values into variables .
#  This is called Unpacking!
fruits=["apple", 'banana', "cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)

#output variables
#The python print() function is often used to output variables.
x="Python is awesome"
print(x)

#output multiple variables.
x="Python"
y="is"
z="awesome"
print(x,y,z)

#You can also use + operator to output multiple variables.
x="Python "
y="is "
z="awesome"
print(x+y+z) # the space character after "Python " and "is " without them the result is 'Pythonisawesome'

#NB: For numbers the + character works as a mathematical operator.
x=5
y=10
print(x+y)

# #You cannot combine a string and a number with the + operator. 
# Python will give an error:TypeError: unsupported operand type(s) for +: 'int' and 'str'
x=5
y="HABIBA"
print(x+y)

# #The best way to output multiple variables in the print() function is to separate them with a COMMA, 
# which even support different data types.
x=5
y="HABIBA"
print(x, y)