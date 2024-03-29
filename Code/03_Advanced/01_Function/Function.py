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


# def greet(name):
#     print(f"Hello {name} Good Morning")
    

# name = input("Enter your name: ")
# greet(name)


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


# Positional Arguments:
# When we call a function, the values we pass are matched to the parameters in order.

# Ye value ke position ke match karta hai.

# def details(name, age):
#     """This function print details"""
#     print(f"Name is: {name} and age is: {age}")
#     return details

# print(details(21, "Manish"))
# Ye name me '21' aur age me "Manish" ko add karega because of position.


# Keyword Arguments:
# When we call a function, we can use the name of the parameter to match the value to the parameter.

# Ye value ke name ko match karta hai.

# def details(name, age):
#     """This function print details"""
#     print(f"Name is: {name} and age is: {age}")
#     return details

# print(details(name="Manish", age=21))
# Ye  name me "Manish" aur age me 21 ko add kara ga. Because yaha pe name aur age ke naam match kar rahe hai.


# We can provide default value for fuunction parameters, making them  optional. If no argument is provided while calling the function then the parameter will take its default value.

# def sum (num1, num2 = 25):
#     """This function adds two numbers"""
#     ans = num1 + num2
#     return ans


# a = int(input("Enter first number: "))
# print("Sum is: ", sum(a))


# Variable Number of Arguments or Arbitrary arguments(*args):

# When you don't know that how many arguments will be passed to the function, then you can use *args.
# *args is used to pass variable number of arguments to a function.
# In *args the arguments are passed as a tuple.

# def add(*args):
#     """This function adds numbers"""
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# output = add(12,45,78,65,1)
# print("The sum of all number is: ", output)


# Keyworded arguments or Arbitrary keyworded arguments(**kwargs):

# When you don't know that how many keyworded arguments will be passed to the function, then you can use **kwargs.
# **kwargs is used to pass variable number of keyworded arguments to a function
# In **kwargs the arguments are passed as a dictionary.


# def student_details(**kwargs):
#     for x,y in kwargs.items():
#         print(x, "is", y)

# student_details(name="Manish", age=21, city="Purnea")
# student_details(name="Anubhav", age=16, city="Jalalgarh")

# Write a fumction to print the sum of one to n number:

# def sum_one_to_n(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     return sum
    

# n = int(input("Enter the number: "))
# print("The sum of one to n number is: ", sum_one_to_n(n))
# n1 = int(input("Enter the number: "))
# print("The sum of one to n1 number is:", sum_one_to_n(n1))


# Nested Function:

# A function defined inside another function is called a nested function.
# Nested function is used to avoid code redundancy and to improve code readability.

# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function

# # Using the nested functions
# closure = outer_function(10)
# result = closure(5)
# print(result)



# def outer(*args):
#     i = int(input("Enter number: "))

#     def inner(*args):
#         x = int(input("Enter number: "))
#         y = int(input("Enter number: "))
#         sum = x + y+i
#         return sum
#     return inner()


# output = outer()
# print(output)



# Pass by value and Pass by reference:


# Python uses pass by object reference, which is a combination of pass by value and pass by reference.

# In pass by value, a copy of an object is passed to the function. This means that any changes made to the object inside the function do not affect the original object.

def addOne(x):
    x = x + 1
    print("Inside finction: ", x)

x = 5
addOne(x)
print("Outside function: ", x)

# In pass by reference, a reference to the object is passed to the function. This means that any changes made to the object inside the function do affect the original object.


def modified_list(list):
    list.append(4)
    print("Inside function: ", list)

list = [1,2,3]
modified_list(list)
print("Outside the function: ", list)


# In python, all objeect are passed by object reference. This means that when you passing an object to a function, the function recive the reference to the object, not the object itself. If the function chage the object, the original object will also changed.


def modified_list(list):
    list.append(4)
    print("Inside function: ", list)

list = [1,2,3]
modified_list(list)
print("Outside the function: ", list)


# Lambda Function:

# A lambda function in Python is an anonymous function defined using the lambda keyword. It's called "anonymous" because it doesn't require a formal name like a regular function defined with def. Lambda functions are typically used for short, simple operations where a full function definition might be overkill.

# Write a program to calculate the cube of a number using lambda function.

number = int(input("Enter a number: "))

cube = lambda x: x**3

result = cube(number)
print("The cube of the number is: ", result)