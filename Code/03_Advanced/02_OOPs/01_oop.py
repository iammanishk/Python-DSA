import math


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

# class MyClass:

#     def __init__(self):
#         self.public_attribute = "This is public Attribute"

#     def public_class(self):
#         return "This is public Method"


# obj1 = MyClass()
# print(obj1.public_attribute)
# print(obj1.public_class())


# ====================== Private Modifiers ======================

# class MyClass:

#     def __init__(self):
#         self.__Private_Attribute = "This is private Attribute"

#     def __Private_method(self):
#         return "This is private Method"

  

# obj = MyClass()
# print(obj.__Private_Attribute)  # This will give an error because it's a Private Attribute and we are trying to access it from outside the class

# print(obj.__Private_method())  # This will give an error because it's a Private method and we are trying to access it from outside the class

 
# ====================== Private Modifiers ======================

# class MyClass:
#     def __init__(self):
#         self._protected_attribute = "I am a protected attribute"

#     def _protected_method(self):
#         return "I am a protected method"
# obj = MyClass()
# print(obj._protected_attribute)  # Output: "I am a protected attribute"
# print(obj._protected_method())    # Output: "I am a protected method"


    

# ====================== Inheritance ======================

# class Shape:
#     def __init__(self, color):
#         self.color = color

#     def area(self):
#         pass # This will be implemented in the child class

#     def display_info(self):
#         return f"This is a {self.color} shape"
    
# class Rectangle(Shape):
#     def __init__(self, color, height, width):
#         super().__init__(color)
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    

# class Circle(Shape):
#     def __init__(self, color, radius):
#         super().__init__(color)
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2   
    
# # Creating object of a subclasses
    
# rectangle = Rectangle("Blue", 5, 4)
# circle = Circle("Red", 7)

# # Using methods inherited from the superclass
# print(f"{rectangle.display_info()} Rectangle")
# print(f"{circle.display_info()} Circle")

# # Using subclass-specific methods
# print(f"The area of the rectangle is {rectangle.area()}")
# print(f"The area of the circle is {circle.area()}")



# ====================== Polymorphism ======================

# class Animal:

#     def speak(self):
#         pass  # This will overridden by subclass

# class Dog(Animal):
#     def speak(self):
#         sound = f"Sound of dog is 'Bark'"
#         return sound
    
# class Cat(Animal):
#     def speak(self):
#         sound = f"Sound of cat is 'Meow'"
#         return sound
    

# cat = Cat()
# dog = Dog()

# print(dog.speak())
# print(cat.speak())

# Method Overriding in Python

# class Animal:
#     def speak(self):
#         return "Animal speaks"


# class Dog(Animal):
#     def speak(self):
#         return "Woof!"


# class Cat(Animal):
#     def speak(self):
#         return "Meow!"


# dog = Dog()
# cat = Cat()

# print(dog.speak())  
# print(cat.speak())


# Operator Overloading:

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
    

# a1 = Vector(2, 3)
# a2 = Vector(4, 5)
# a3 = a1 + a2

# print(a3.y + a3.x)


# Abstraction

# class Car:

#     def start(self):
#         print("The car has started")

#     def accellarate(self):
#         print("The car is accellarating")

#     def stop(self):
#         print("The car has stopped")


# # creating car object

# my_car = Car()

# # Intreract with car
# my_car.start()
# my_car.accellarate()
# my_car.stop()



# Encapsulation
class Car:

    def __init__(self, make, model):
        self._model = model  # Protected Attribute
        self._make = make    # Protected Attribute

    def display_info(self):
        return f"This is a {self._make} {self._model} car"
    
    def drive(self):
        return f"Driving the car"
    

# Creating the object
car = Car("Toyota", "Corolla")


print(car.display_info())  # Accessing public method to interact with the car object

print(car._make)  # Attempting to access protected attribute directly (not recommended)
print(car.drive())  # Accessing public method to interact with the car object