# ========================================================= DICTIONARY =========================================================

# A dictionary is a data structure that allows you to store and retrieve values using a key. In a Python dictionary, each key is associated with a value, forming a key-value pair.


# ----------------------------------- Creating a Dictionary -----------------------------------


# Creating a dictionary is as simple as placing items inside curly braces {} separated by commas.

student = {
    'name' : "Manish Yadhuvanshi",
    'age' : 21,
    'courses' : ["Python", "Machine Learning", "Data Science"],
    'is_active' : True
}

# print(student)

# Here key is 'name' and value is 'Manish Yadhuvanshi' and so on. You can access the values using their keys.


# Accessing the dictionary:
# You can access the items of a dictionary by referring to its key name, inside square brackets []. If the item is not found, it will raise a KeyError.

# print("Name of student: ", student['name'])
# print("Age of student: ", student['grade'])

# If you try to access a key that doesn’t exist in the dictionary, Python will raise an error. 
# To avoid this we use get() method which returns 'None' if the key does not exist in the dictionary.

# print("Phone number of student: ", student.get('phone'))


# Modifying Values:

# You can change the value of a specific item by referring to its key name.

student['age'] = 20
# print(student)

# Adding New Key-Value Pairs:

# Adding an item to the dictionary is done by using a new index key and assigning a value to it.

student['email'] = "iammaanisshhh@gmail.com"
student['grade'] = "A+"
# print(student)

# You can also use update() method to add new key-value pairs to the dictionary.

address = {
    'city' : "Purnea",
    'state' : "Bihar",
    'country' : "India"
}

student.update(address)
# print(student)

# Removing Key-Value Pairs:

# Removing an item from the dictionary is done by using the pop() method. This method removes the item with the specified key name.

# student.pop('grade') # This removes the whole pair (key & Value).
# print(student)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead).

# student.popitem()
# print(student)

# You can remove the key-value pair using del keyword also.
# del student['email']
# print(student)

# You can delet all the key-value pairs using clear() method.

# student.clear()
# print(student)

# Checking if the item is present in the dictionary or not:

# To determine if a specified key is present in a dictionary use the 'in' keyword.

# if 'age' in student:
#     print("Yes, 'age' is one of the keys in the student dictionary")
# else:
#     print("No, 'age' is not any of the keys in the student dictionary")

# Printing the elements of the dictionary:

# You can print all the keys of the dictionary using keys() method.
# print(student.keys())

# You can print all the values of the dictionary using values() method.
# print(student.values())

# You can print all the key-value pairs of the dictionary using items() method.
# print(student.items())

# Looping through a dictionary:
for x in student:
    print(x) # This prints all the keys of the dictionary.

for x in student.items():
    print(x) # This prints all the key-value pairs of the dictionary.

for x,y in student.items():
    print(x,y) # This prints all the key-value pairs of the dictionary in a more readable format.


