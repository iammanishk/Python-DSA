# Write a program to display the last digit of the number given by the user.



# +++++++++++++++++++++++++++++++++++++++++++++++++ CODE +++++++++++++++++++++++++++++++++++++++++++++++++


num = int(input("Enter the number: "))  # this will take the number from the user

last_digit = (num % 10) # this will find the last digit of the number
print("The last digit of the number is: ",  last_digit)