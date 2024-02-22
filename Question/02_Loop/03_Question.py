# Write a program to print the table of n upto 10, but skip the given iteration

n = int(input("Enter the number to print the table: "))
skip_iteration = int(input("Enter the iteration to skip: "))


for i in range(1, 11):
    if i == skip_iteration:
        continue
    print(n,"X",i,"=",n*i)
