
# class Student:

#     def set_name(self, name, age):
#         self.name = name
#         self.age = age

#     def get_name(self):
#         return self.name, self.age
    

# student1 = Student()
# student1.set_name("Manish", 21)
# print(student1.get_name())




# ------------------------------------------------------------------- Class Constructor -------------------------------------------------------------------

# height = int(input("Enter the height of the rectangle:  "))
# width = int(input("Enter the width of the rectangle:  "))

# class Rectangle:  

#     def __init__(self, height, width):
#         self.height = height
#         self.width = width

#     def area(self):
#         area_of_rectangle = self.width * self.height
#         return area_of_rectangle
    
#     def perimeter(self):
#         perimeter_of_rectangle = 2*(self.width + self.height)
#         return perimeter_of_rectangle
    

# rectangle1 = Rectangle(height, width)
# print(f"The area of the rectangle is: {rectangle1.area()}")
# print(f"The perimeter of the rectangle is: {rectangle1.perimeter()}")




# ------------------------------------------------------------------- Instance -------------------------------------------------------------------


# class Student():
#     def __init__(self, name):
#         self.name = name    # Class Attribute
        

#     def show_name(self):
#         return self.name
    

# student1 = Student("Manish")
# student1.show_name()
# print(student1.show_name())
# student1.roll_number = 1321139
# print(student1.roll_number)   # Instance Attribute
        

# student2 = Student("Chotu")
# student2.show_name()
# print(student2.show_name())    
# student2.roll_number = 1321138    
# print(student2.roll_number)  # Instance Attribute





# ------------------------------------------------------------------- Access Modifiers -------------------------------------------------------------------


# ====================== Public Modifiers ======================

class MyClass:

    def __init__(self):
        self.public_attribute = "This is public Attribute"

    def public_class(self):
        return "This is public Method"


obj1 = MyClass()
print(obj1.public_attribute)
print(obj1.public_class())


# ====================== Private Modifiers ======================

class MyClass:

    def __init__(self):
        self.__Private_Attribute = "This is private Attribute"

    def __Private_method(self):
        return "This is private Method"

  

obj = MyClass()
print(obj.__Private_Attribute)  # This will give an error because it's a Private Attribute and we are trying to access it from outside the class

print(obj.__Private_method())  # This will give an error because it's a Private method and we are trying to access it from outside the class

 
# ====================== Private Modifiers ======================

class MyClass:
    def __init__(self):
        self._protected_attribute = "I am a protected attribute"

    def _protected_method(self):
        return "I am a protected method"
obj = MyClass()
print(obj._protected_attribute)  # Output: "I am a protected attribute"
print(obj._protected_method())    # Output: "I am a protected method"


    



