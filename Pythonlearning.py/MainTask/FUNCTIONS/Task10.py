# TASK 10: Using Python
# Write a program that calculates the total stock in a company from the array/list 
# below if we know that the stock is the last digit in every array/list.
# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]
# Nested list containing product information

# Nested list containing product information
prods = [['omo', '30kshs', '300'], ['milk', '50kshs', '200'], ['bread', '45kshs', '359'], ['coffee', '5kshs', '79']]

def calculate_total_stock(products):
    total_stock = 0

    for i in products:
        stock = int(i[2])  # Extracting the stock from the last element
        total_stock += stock

    return total_stock

# Calling the function to calculate total stock
total_stock = calculate_total_stock(prods)
print("Total stock in the company:", total_stock)
