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

print(student)

# Here key is 'name' and value is 'Manish Yadhuvanshi' and so on. You can access the values using their keys.

print("Name of student: ", student['name'])
print("Age of student: ", student['age'])