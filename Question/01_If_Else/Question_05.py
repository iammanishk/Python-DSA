# Write a program to display 'Hello' if the number entered by the user is multiple of 5 otherwise display 'Bye'.

num = int(input("Enter the number: "))

if num % 5 == 0:
    print("Hello")
else:
    print("Bye")