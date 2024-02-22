# Write a program to keep asking the user to enter the number until the user enters the number between 1 to 10.

while True:
    number = int(input("Enter the numberbetween 1 to 10: "))
    if 1 <= number <= 10:
        break
    else:
        print("Please enter the number between 1 to 10.")

print("The number you entered is: ", number)