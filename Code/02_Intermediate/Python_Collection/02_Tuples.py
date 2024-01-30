# ========================================================= TUPLES =========================================================


# Tuples are similar to lists but they are immutable means once you assign a value to it you cannot change or modify that value again.
# Tuples are defined by enclosing elements within parentheses  `( )`, separated by commas. 
# Tuples are faster than lists because of static in nature. They do not support changes to their size, and they cannot be changed after creation.
# They can contain any type of objects, including other tuples.



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  CODE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Creating a tuple

tup = (12,0.7,"Manish")
# print(tup)

nested_tup = (12, 0.7, ("Manish", "Yadhuvanshi"), (854327, "BCA", ("C++", "Python")) )
# print(nested_tup)
new_nestde_tup = nested_tup[2][1]
# print(new_nestde_tup)


# Creating a tuple with single element
# You can create a tuple with single element by putting a comma after the element. This is called a singleton tuple.

tup = (12) # this is not a tuple
print(type(tup))
tup = (12,) # this is a tuple
print(type(tup))
