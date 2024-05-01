days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
#1. Find wednesday using an index
days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
print(days[2])

#2. Using a function a find the length of the tuple.
days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
print(len(days))

#3. Replace Thursday with Thur

#UPDATE MUST USE =
days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
my_list=list(days) # CONVERT IT TO LIST
print(my_list)
my_list[3]="Thur"
print(my_list)
#convert it back to tuple


my_list=tuple(my_list) # CONVERT IT TO tuple
print(my_list)