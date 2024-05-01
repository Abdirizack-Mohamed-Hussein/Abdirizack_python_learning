# TASK 8: Using Python ....write this code inside a function.
# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”.
# Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point 
# and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, 
# the function should print: “License suspended”.



# Prompting the user for input
speed = float(input("Enter the speed of the car: "))

def check_speed(speed):
    speed_limit = 70
    demerit_points = 0

    if speed <= speed_limit:
        print("Ok")
    else:
        demerit_points = (speed - speed_limit) // 5
        print(f"Points: {demerit_points}")

        if demerit_points > 12:
            print("License suspended")

# Calling the function to execute the code
check_speed(speed)
