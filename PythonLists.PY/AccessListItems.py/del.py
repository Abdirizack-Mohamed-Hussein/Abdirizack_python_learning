# The del keyword also removes the specified index:

# Example
# Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.

# Example
# Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List
# The clear() method empties the list.

# The list still remains, but it has no content.

# Example
# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
