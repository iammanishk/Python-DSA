# ========================================================= CONDITIONAL OPERATORS =========================================================

# ---------------------------------------------------------- IF ELSE ----------------------------------------------------------


# Write a program to check whether a number is positive, negative or zero using if else.

# number = int(input("Enter any number! "))

# if number > 0:
#     print("The number is positive!")
# elif number == 0:
#     print("The number is zero!")
# elif number < 0:
#     print("The number is negative!")
# else:
#     print("Enter a valid number")


# Write a program to check that a positive integer is eeven or odd
    
number = int(input("Enter any number! "))

if number > 0:
    if number % 2 == 0:
        print("The number is even!")
    else:
        print("The number is odd!")
else:
    print("Enter a valid number")