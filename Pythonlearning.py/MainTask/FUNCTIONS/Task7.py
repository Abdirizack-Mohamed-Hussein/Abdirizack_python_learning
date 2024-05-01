# TASK 7: Using Python ....write this code inside a function.
# Write that prompts the user to input student marks. The input should be between 0 and 100.
# Then output the correct grade: 
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

def calculate_grade():
    # Prompting the user for input
    marks = float(input("Enter student marks: "))

    # Checking if marks are between 0 and 100
    if 0 <= marks <= 100:
        # Determining the grade based on marks
        if marks > 79:
            grade = 'A'
        elif 60 <= marks <= 79:
            grade = 'B'
        elif 50 <= marks <= 59:
            grade = 'C'
        elif 40 <= marks <= 49:
            grade = 'D'
        else:
            grade = 'E'

        # Outputting the grade
        print(f"The grade is: {grade}")
    else:
        print("Marks should be between 0 and 100.")

# Calling the function to execute the code
calculate_grade()