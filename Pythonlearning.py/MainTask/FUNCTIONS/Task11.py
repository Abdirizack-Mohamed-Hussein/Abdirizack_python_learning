# TASK 11: Using Python ...write this code inside a function.
# Write a program that takes the date of birth of a person 
# and the program outputs the age in terms of years,months,days TODAY.

from datetime import datetime
# Prompting the user for input (date of birth)
dob_str = input("Enter your date of birth (YYYY-MM-DD): ")



def calculate_age(birth_date):
    # Getting the current date
    current_date = datetime.now()

    # Calculating the difference between current date and birth date
    age= current_date - birth_date

    # Calculating age in years, months, and days
    age_years = age.days // 365
    age_months = (age.days % 365) // 30
    age_days = (age.days % 365) % 30

    return age_years, age_months, age_days

# Calling the function to calculate age
age_years, age_months, age_days = calculate_age(dob)

# Printing the age
print(f"Age: {age_years} years, {age_months} months, {age_days} days")
