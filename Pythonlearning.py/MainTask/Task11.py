# TASK 11: Using Python
# Write a program that takes the date of birth of a person 
# and the program outputs the age in terms of years,months,days TODAY.
# Get the current date
current_year = 2024
current_month = 2
current_day = 6

# Get the user's date of birth
birth_year = int(input("Enter the year of birth: "))
birth_month = int(input("Enter the month of birth: "))
birth_day = int(input("Enter the day of birth: "))

# variables to store age components
years = 0
months = 0
days = 0

# Check if the birthday has occurred this year
if current_month >= birth_month and current_day >= birth_day:
    years = current_year - birth_year
else:
    years = current_year - birth_year - 1

# Calculate remaining months and days
for i in range(birth_month, current_month):
    months += 1

if current_month == birth_month and current_day < birth_day:
    months -= 1

if current_day < birth_day:
    days = 30 - (birth_day - current_day)
else:
    days = current_day - birth_day

# Display the age
print(f"Age: {years} years, {months} months, {days} days")
