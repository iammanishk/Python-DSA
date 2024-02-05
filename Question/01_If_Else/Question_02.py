# Write a program to check whether a number given by user is positive, negitive or zero. 

num = int(input("Enter the number: "))

if num > 0:
    print("The number give by the user is Positive.")
elif num < 0:
    print("The number given by the user is Negitive.")
elif num == 0:
    print("The number given by the user is Zero.")
else:
    print("Enter valid number")
    