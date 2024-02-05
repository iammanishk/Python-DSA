# Write a program to check the last digit of the number is divisible by 9 or not. (number is given by the user)

# +++++++++++++++++++++++++++++++++++++++++++++++++ CODE +++++++++++++++++++++++++++++++++++++++++++++++++

num = int(input("Enter the number: "))  # this will take the number from the user

last_digit = (num % 10) # this will find the last digit of the number

if last_digit % 9 == 0:  # this will check the last digit is divisible by 9 or not
    print("The last digit is divisible by 9.")
else:
    print("No the last digit is not divisible by 9.")