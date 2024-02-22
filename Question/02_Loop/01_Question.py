# Write a program that count all the positive number in a list and print their sum

number = [1,5,-4,-5,0,9,-25,0,65,75]
print(number)

count_of_positive = 0
sum_of_positive = 0
for i in number:
    if i > 0:
        print("All the positive number are: ", i)
        count_of_positive += 1
        sum_of_positive += i
print("The number of all the positive number is: ", count_of_positive)
print("The sum of all the positive number is: ", sum_of_positive)



