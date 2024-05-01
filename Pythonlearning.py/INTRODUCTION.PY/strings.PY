# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:
print("Hello")
print('Hello')
# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print(a)

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:
# You can use three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
# EXAMPLE
# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])
# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Loop through the letters in the word "banana":
for x in "banana":
  print(x)

#   String Length
# To get the length of a string, use the len() function.
#  The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
# Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)

# TASKS TECH CAMP
course= 'Python For Beginners'
print(course)

#To get first index of the character
course= 'Python For Beginners'
print(course[0])
print(course[1])
print(course[2])
print(course[3])
print(course[4])
print(course[5])
print(course[6])
print(course[7])
print(course[8])
print(course[9])
print(course[10])
print(course[11])
print(course[12])
print(course[13])
print(course[14])
print(course[15])
print(course[16])
print(course[17])
print(course[18])
print(course[19])
#NEGATIVES
print(course[-1])
print(course[-2])
print(course[-3])
print(course[-4])
print(course[-5])
print(course[-6])
print(course[-7])
print(course[-8])
print(course[-9])
print(course[-10])
print(course[-11])
print(course[-12])
print(course[-13])
print(course[-14])
print(course[-15])
print(course[-16])
print(course[-17])
print(course[-18])
print(course[-19])
print(course[-20])

#slicing # the beginning and last character
course= 'Python For Beginners'
print(course[0:3]) #ignores the 3 character
print(course[1:3])
print(course[0:3])
print(course[0:])
print(course[:0])
print(course[:5])
print(course[:])   #returns all characters

#Very important
course= 'Python For Beginners'
another= course[:]
print(another)

#EXAMPLE
name=  "JENNIFER"
print(name[1:-1])

#email
email= "mohamedabdirizak049@gmail.com"
print(email[19:-9])