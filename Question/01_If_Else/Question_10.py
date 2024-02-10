# Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria:



# Cost Price of the bike (in Rs.)                Road Tax 

# More than 100000                               15% of the cost price
# More than 50000 and less than 100000           10% of the cost price
# Less than 50000                                5% of the cost price

# +++++++++++++++++++++++++++++++++++++++++++++++++ CODE +++++++++++++++++++++++++++++++++++++++++++++++++

cost_price = int(input("Enter the cost price of the bike: "))
tax = 0

if cost_price > 100000:
    tax = (cost_price / 100) * 15
    print("The road tax to be paid is: ", tax)
elif cost_price > 50000 and cost_price < 100000:
    tax = (cost_price / 100) * 10
    print("The road tax to be paid is: ", tax)
elif cost_price < 50000:
    tax = (cost_price / 100) * 5
    print("The road tax to be paid is ", tax)
else:
    print("Invalid Input")

    