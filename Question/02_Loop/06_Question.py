# Write a program to calculate the factorial of a number using while loop.

number = int(input("Enter the number to calculate the factorial: "))

factorial = 1 # if this will 0 the all you answer will be 0

while number > 0:
    factorial *= number
    number -= 1

print("The factorial of the given number is: ", factorial)

