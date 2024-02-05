# Write a program to check that the persion is eligible for voting or not.(accept the age from user)

age = int(input("Enter your age: "))  # this will take the age from the user

if age >= 18:
    print("You are eligible for voting")

else:
    print("You are under age of 18, so you are not eligible for voting")