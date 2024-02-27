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