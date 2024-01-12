# ========================================================= CONDITIONAL OPERATORS =========================================================

# ---------------------------------------------------------- IF ELSE ----------------------------------------------------------


# Write a program to check whether a number is positive, negative or zero using if else.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CODE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# number = int(input("Enter any number! "))

# if number > 0:
#     print("The number is positive!")
# elif number == 0:
#     print("The number is zero!")
# elif number < 0:
#     print("The number is negative!")
# else:
#     print("Enter a valid number")


# Write a program to check that a positive integer is even or odd
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CODE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    
# number = int(input("Enter any number! "))

# if number > 0:
#     if number % 2 == 0:
#         print("The number is even!")
#     else:
#         print("The number is odd!")
# else:
#     print("Enter a valid number")

# Write a program that will print the profit or loss of the product based on the cost price and sellling price
  
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CODE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# cost_Price = int(input("Enter the cost price of the product \n"))
# sellling_Price = int(input("Enter the selling price of the product \n"))

# if sellling_Price > cost_Price:
#     profit = sellling_Price - cost_Price
#     print("You have the profit of ", profit , "Rupees")
# elif cost_Price > sellling_Price:
#     loss = cost_Price - sellling_Price
#     print("You are in the loss of ", loss, "Rupees")
# elif cost_Price == sellling_Price:
#     print("\nYou are not in either Profit or Loss")
# else:
#     ("Enter valid data")



# Write a proggram to find the greatest number using nested if else
  
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CODE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

num1 = int(input("Enter number one \n"))
num2 = int(input("Enter number two \n"))
num3 = int(input("Enter number three \n"))

if num1 > num2:
    if num1 > num3:
        print("Number one is greatest ", num1)
    else:
        print("Number three is greatest ", num3)
else:
    if num2 > num3:
        print("Number two is greatest ", num2)
    else:
        print("Number three is greatest ", num3)