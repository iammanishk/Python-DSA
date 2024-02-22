# Write a program to calcuate the sum of even number upto n and also print the even nuber in a list
n = int(input("Enter the number: "))
sum_of_even = 0
number_of_even = 0
list = []

for i in range(1, n+1):
    if i % 2 == 0:
        number_of_even += 1
        list.append(i)
        sum_of_even += i
print("The number of even number is: ", number_of_even)
print("The even number are: ", list)
print("The sum of even number is: ", sum_of_even)