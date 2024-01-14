# ========================================================= MATCH CASE =========================================================

# Make a calculator using match statement
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CODE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

num1 = int(input("Enter nnummber one \n"))
num2 = int(input("Enter number two \n"))
operator = input("Enter any oprtator \n")

match operator:
    case "+":
        print("Sum of num1 and num2 is: ", num1 + num2)
    case "-":
        print("Subtraction of num1 and num2 is: ", num1 - num2)
    case "*":
        print("Multiplication of num1 and num2 is: ", num1 * num2)
    case "/":
        print("Division of num1 and num2 is: ", num1 / num2)
    case "%":
        print("Modulus of num1 and num2 is: ", num1 % num2)
    case _:
        print("Enter valid operator")