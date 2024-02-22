# Write a program to chech if the number is prime or not using 

number = int(input("Enter the number to check if it is prime or not: "))
is_Prime = True


if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_Prime = False
            break
print("The number is prime: ", is_Prime)
            