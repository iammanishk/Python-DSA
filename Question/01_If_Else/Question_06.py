# Wirite a program  to calculate the electricity bill (accept number of unit from user) according to the following criteria:

# Unit                                         Price
# First 100 units                             no charge
# Next 100 units                              10/- per unit
# Above 200 units                              15/- per unit


# +++++++++++++++++++++++++++++++++++++++++++++++++ CODE +++++++++++++++++++++++++++++++++++++++++++++++++

electric_unit = int(input("Enter the unit of electricity: "))  # this will take the unite of the electricity

if electric_unit <= 100:
    electricity_bill = electric_unit * 5
    print("Electricity Bill is: ", electricity_bill)
elif electric_unit > 100 and electric_unit <= 200:
    electricity_bill = (100 * 5) + ((electric_unit - 100) * 10)
    print("Electricity Bill is: ", electricity_bill)
elif electric_unit > 200:
    electricity_bill = (100 * 5) + (100 * 10) + ((electric_unit - 200) * 15)
    print("Electricity Bill is: ", electricity_bill)
else:
    print("Enter a valid unit of electricity.")

    

    