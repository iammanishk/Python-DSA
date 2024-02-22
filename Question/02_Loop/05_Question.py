# Write a program to find the first non-repeating charaacter.

# string = input("Enter the word: ")
# length = len(string)

# for i in string:
#     if string.count(i) == 1:
#         print("The first non-repeating character is: ", i)
#         break



# ------------------------------------------------------------------------------------------------------------

# Write a program to find the all non-repeating charaacter.
    

# string = input("Enter the word: ")
# length = len(string)

# for i in string:
#     if string.count(i) == 1:
#         print("The non-repeating character is: ", i)
        


# ------------------------------------------------------------------------------------------------------------


# Write a program to find the all repeating charaacter.

string = input("Enter the word: ")

for i in string:
    if string.count(i) > 1:
        print("The repeating character is: ", i)