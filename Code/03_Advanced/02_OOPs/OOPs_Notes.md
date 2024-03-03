# This is the proper containing all the parts of the OOPs concept.

- Object-oriented programming (OOP) is a programming paradigm that organizes code into objects, which represent real-world entities, and allows these objects to interact with each other. 

### Class:
- A class is like a blueprint that defines the properties (attributes) and behaviors (methods) that objects will have.
### Object:
- An object is an instance of a class. It represents a specific example of the class, with its own unique state and behavior.
### Attributes: 
- Attributes are variables that store data associated with objects.
### Methods: 
- Methods are functions defined within a class that perform actions on objects.

- Example of class and object that takes height and width and return area and perimeter

```
Example: 

height = int(input("Enter the height of the rectangle:  "))
width = int(input("Enter the width of the rectangle:  "))

class Rectangle:

    def set_dimension(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area_of_rectanle = self.width * self.height
        return area_of_rectanle
    
    def perimeter(self):
        perimeter_of_rectangle =2 * (self.width + self.height)
        return perimeter_of_rectangle
    

rectangle1 = Rectangle()
rectangle1.set_dimension(height, width)
print(f"The area of the rectanlge is: {rectangle1.area()}")
print(f"The perimeter of the rectanlge is: {rectangle1.perimeter()}")
```

- `self` is predefined  python variable which refers to the instance of the class. It binds an attribute with the method so
In this example `Rectangle` is a class and `set_dimension`, `area`, and `perimeter` are methods in the class. The attributes are `width` and `height`. And `rectangle1` is object.

### Class Constructor:
- Class constructor is a special function that gets invoked every time an object is created for that class
```
Syntex:

class ClassName:
    def __init__(self, parameter1, parameter2):
    # Code to execute when creating an object goes here
```

```
Example: 

height = int(input("Enter the height of the rectangle:  "))
width = int(input("Enter the width of the rectangle:  "))

class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        area_of_rectangle = self.width * self.height
        return area_of_rectangle
    
    def perimeter(self):
        perimeter_of_rectangle = 2*(self.width + self.height)
        return perimeter_of_rectangle
    

rectangle1 = Rectangle(height, width)
print(f"The area of the rectangle is: {rectangle1.area()}")
print(f"The perimeter of the rectangle is: {rectangle1.perimeter()}")
```

### Instance:
- An Instance are specific to particular instance or object
- An instance is a concrete realization of a class, with its own unique state and behavior, based on the blueprint provided by the class.

```
Enample:

class Student():
    def __init__(self, name):
        self.name = name    # Class Attribute
        

    def show_name(self):
        return self.name
    

student1 = Student("Manish")
student1.show_name()
print(student1.show_name())
student1.roll_number = 1321139
print(student1.roll_number)   # Instance Attribute
        

student2 = Student("Chotu")
student2.show_name()
print(student2.show_name())    
student2.roll_number = 1321138    
print(student2.roll_number)  # Instance Attribute
```


###  Access Modifiers:
- Access modifiers are used to control the accessibility of attributes and methods within a class. 
- Although Python does not have traditional access modifiers like public, private, or protected as in some other languages like Java, it provides a convention for indicating the accessibility of class members. 
- There are three types of access modifiers
1. Public:  By default, all attributes and methods in a class are considered public and can be accessed from outside the class.
```
Example of Public Modifiers:

class MyClass:

    def __init__(self):
        self.public_attribute = "This is public Attribute"

    def public_class(self):
        return "This is public Method"


obj1 = MyClass()
print(obj1.public_attribute)
print(obj1.public_class())
```
2.  Private: Attributes and methods prefixed with a double underscore `__` are considered private, indicating that they should not be accessed from outside the class. Python enforces name mangling for private attributes, meaning their names are mangled to include the class name to make them harder to access directly from outside the class.
```
Example of Private Modifiers:

class MyClass:

    def __init__(self):
        self.__Private_Attribute = "This is private Attribute"

    def __Private_method(self):
        return "This is private Method"

  

obj = MyClass()
print(obj.__Private_Attribute)  # This will give an error because it's a Private Attribute and we are trying to access it from outside the class

print(obj.__Private_method())  # This will give an error because it's a Private method and we are trying to access it from outside the class
```
3.  Protected: Attributes and methods prefixed with a single underscore ` _ ` are considered protected, indicating that they are intended for internal use within the class or its subclasses. However, they can still be accessed from outside the class.
```
Example of Protected Modifiers:

class MyClass:
    def __init__(self):
        self._protected_attribute = "I am a protected attribute"

    def _protected_method(self):
        return "I am a protected method"
obj = MyClass()
print(obj._protected_attribute)  # Output: "I am a protected attribute"
print(obj._protected_method())    # Output: "I am a protected method"


```

