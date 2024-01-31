# ========================================================= TUPLES =========================================================


# Tuples are similar to lists but they are immutable means once you assign a value to it you cannot change or modify that value again.
# Tuples are defined by enclosing elements within parentheses  `( )`, separated by commas. 
# Tuples are faster than lists because of static in nature. They do not support changes to their size, and they cannot be changed after creation.
# They can contain any type of objects, including other tuples.



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  CODE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Creating a tuple

tup = (12,0.7,"Manish")
print(tup)

nested_tup = (12, 0.7, ("Manish", "Yadhuvanshi"), (854327, "BCA", ("C++", "Python")) )
print(nested_tup)
new_nestde_tup = nested_tup[2][1]
print(new_nestde_tup)


# Creating a tuple with single element
# You can create a tuple with single element by putting a comma after the element. This is called a singleton tuple.

single_element_tup = (12) # this is not a tuple
print(type(tup))
single_element_tup = (12,) # this is a tuple
print(type(tup))


# Accessing elements of a tuple
# You can access tuple elements by referring to the index number, inside square brackets `[]`.

print("Accessing elements using Index: ", tup[2])
print("Accessing element form backword: ",tup[-1])

print("Accessing element from nested tuple:", nested_tup[3][2][1])
print("Accessing element by using range index:", nested_tup[1:4])


# Checking if an element exists in tuple:

if "BCA" in nested_tup[3]:
    print("Yes, 'BCA' is in the tuple")
else:
    print("No, 'BCA' is not in the tuple")




# Changing a Tuple
# Unlike lists, tuples are immutable.
# This means that elements of a tuple cannot be changed once they have been assigned. But, if the element is itself a mutable data type like list, its nested items can be changed.
    
# Changing tuple values
# You can convert the tuple into a list, change the list, and convert the list back into a tuple.


print(tup)
tuple_list = list(tup)
tuple_list[2] = "Yadhuvanshi"
tup = tuple(tuple_list)
print("Tuple after changing value : ", tup)


# Adding items to a tuple
# Since tuples are immutable, you cannot add or remove items from tuples like lists.
# But you can add two or more tuples together.

tup1 = (12, 0.7, "Manish")
tup2 = (854327, "BCA", "C++")
tup3 = tup1 + tup2
print("Tuple after adding two tuples: ", tup3)


# Tuple Packing and Unpacking:
# In packing, we place value into a new tuple while in unpacking we extract those values back into variables.

# Packing:
tup1 = ("Manish", 854327, "BCA")

# This will create a tuple with these three elements.
# Now to unpack the elements of this tuple we can use this assignment operation


# Unpacking:
# tuple unpacking involves extracting the values back into variables.

name, pin, course = tup1
print(pin)

# Slicing of Tuple:

fruit = ("Apple", "Banana", "Cherry", "Orange", "Kiwi", "Melon", "Mango")

first_three_fruit = fruit[0:3]
print(first_three_fruit)
print(len(first_three_fruit))











# ------------------------------------------------- PRACTICE -------------------------------------------------
