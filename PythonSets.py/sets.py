# Set
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Note: Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.


days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
print(days)

# Remove friday and sunday from the set using methods.
days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
days.remove("friday")
days.remove("sunday")
print(days)
# Add them back to the set
days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
days.add("friday")
days.add("sunday")
print(days)