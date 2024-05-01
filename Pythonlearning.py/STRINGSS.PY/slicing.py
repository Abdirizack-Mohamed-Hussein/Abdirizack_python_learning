# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

# Example
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])  #Note: The first character has index 0.

# Slice From the Start
# By leaving out the start index, the range will start at the first character:
b = "Hello, World!"
print(b[:5])

# Slice To the End
# By leaving out the end index, the range will go to the end:
# Example
# Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Example
# Get the characters:

# From: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])

#slicing # the beginning and last character
course= 'Python For Beginners'
print(course[0:3]) #ignores the 3 character
print(course[1:3])
print(course[0:3])
print(course[0:])
print(course[:0])
print(course[:5])
print(course[:])   #returns all characters
