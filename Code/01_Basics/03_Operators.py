# ========================================================= OPERATROS =========================================================

# You can take input form user by using 'input' 
name = input("What is your name? ")
print("Hello " + name)


# OPERATORS
# Operators in python are symbols that perform operations on variables when they appear together in an expression

# 1. Arithmetic Operators:

# - `+` : Addition
# - `-` : Subtraction
# - `*` : Multipication
# - `/` : Division
# - `%` : Modulus i.e., remainder after division
# - `//` : Floor Division - result is the quotient rounded down to the nearest integer
# - `**` : Exponentiation

a = 10
b = 3

sum_result = a + b       # 13
difference_result = a - b  # 7
product_result = a * b    # 30
division_result = a / b   # 3.333...
remainder_result = a % b  # 1
floor_division_result = a // b  # 3
exponentiation_result = a ** b  # 1000

# print(sum_result)
# print(difference_result)
# print(product_result)
# print(division_result)
# print(remainder_result)
# print(floor_division_result)
# print(exponentiation_result)


# 2. Comparison Operators:

# - `==` : Equal to
# - `!=` : Not equal to
# - `<` : Less than
# - `>` : Greater than
# - `<=` : Less than equal to
# - `>=` : Greater than equal to

x = 5
y = 10

is_equal = x == y        # False
not_equal = x != y       # True
less_than = x < y        # True
greater_than = x > y     # False
less_than_equal = x <= y  # True
greater_than_equal = x >= y  # False

# print(is_equal)
# print(not_equal)
# print(less_than)
# print(greater_than)
# print(less_than_equal)
# print(greater_than_equal)


# 3. Logical Operators:
#    - and (Logical AND)
#    - or (Logical OR)
#    - not (Logical NOT)


p = True
q = False
logical_and = p and q     # False
logical_or = p or q       # True
logical_not = not p       # False

print(logical_and)
print(logical_or)
print(logical_not)
