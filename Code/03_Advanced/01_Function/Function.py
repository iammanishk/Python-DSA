# ========================================================= FUNCTION =========================================================

# In python, a function is a reusable code that perform a specific task.
# A function is a block of code which only runs when it is called.
# Function helps in organizing code, making it more readable,reusable, modular and maintainable.   

# --------------------------------------- Defining Function:---------------------------------------

# def function_name(parameters):
#     Statements
#     return expression

# --------------------------------------- Calling Function:---------------------------------------
# Use the function name followed by parentheses to call it.
# Function arguments are the values received by the function when it is invoked.


def greet(name):
    print("Hello", name, "Good Morning!")
    

name = input("Enter your name: ")
greet(name)


# --------------------------------------- Return Statement:---------------------------------------
# The return statement is used to exit a function and go back to the place from where it was called.
# The docstring ("""...""") provides a brief description of the function.

# Syntax:
# return expression


# def sum(num1, num2):
#     """This function adds two numbers"""
#     ans = num1 + num2
#     return ans

# WAP to find the sum of two numbers using function.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("The sum is: ", sum(num1, num2))


# We can provide default value for fuunction parameters, making them  optional. If no argument is provided while calling the function then the parameter will take its default value.

def sum (num1, num2 = 25):
    """This function adds two numbers"""
    ans = num1 + num2
    return ans


a = int(input("Enter first number: "))
print("Sum is: ", sum(a))