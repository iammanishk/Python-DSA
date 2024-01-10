# ========================================================= DATATYPES =========================================================

# Python has the following data types built-in by default, in these categories:

name = "Manish"
rollNumber = 39
marks = 95.5
isPassed = True
isFail = False
subjects = ["Maths", "Physics", "Chemistry"]
student = {"name": "Manish", "rollNumber": 39, "marks": 95.5, "isPassed": True, "isFail": False, "subjects": ["Maths", "Physics", "Chemistry"]}
none = None



# print("Name of the variable is : ", name)
# print("Type of the variable is : ", type(name))

# print("Subject of the variable is : ", subjects)
# print("Type of the variable is : ", type(subjects))

# You can concatenate same dataType with '+' this sign
print("Name of the student is " + name + " Yadhuvanshi")

# You can't concatenate different dataType with '+' this sign, but you can doo it by using this ','
print("Name of the student is ", name, " and roll number is ", rollNumber, "and marks are ", marks)


# You can also print with seperator
print(name,rollNumber,marks, sep="-")


# You cha check the ascii value by usin ord function
char = "M"
print(ord(char))

# You can check the value corsponding to the ascii value by usin chr function
ascii = 64
print(chr(ascii)) # output of this is '@'