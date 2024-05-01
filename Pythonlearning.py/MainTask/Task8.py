# TASK 8: Using Python 
# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. 
# Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point 
# and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. 
# If the driver gets more than 12 points, the function should print: “License suspended”.

# Taking input for car speed
speed = float(input("Enter the speed of the car (in km/h): "))

# Speed limit
speed_limit = 70

# Demerit points for every 5 km/h above the speed limit
demerit_points_per_5kmh = 1

# Checking the speed and calculating demerit points
if speed <= speed_limit:
    print("Ok")
else:
    excess_speed = speed - speed_limit
    demerit_points = round(excess_speed/ 5)  # Calculating demerit points for every 5 km/h above the limit

    # Displaying the result
    if demerit_points > 12:
        print(f"Points: {demerit_points}. License suspended.")
    else:
        print(f"Points: {demerit_points}")
