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
1. __Public__:  By default, all attributes and methods in a class are considered public and can be accessed from outside the class.
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
2.  __Private__: Attributes and methods prefixed with a double underscore `__` are considered private, indicating that they should not be accessed from outside the class. Python enforces name mangling for private attributes, meaning their names are mangled to include the class name to make them harder to access directly from outside the class.
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
3.  __Protected__: Attributes and methods prefixed with a single underscore ` _ ` are considered protected, indicating that they are intended for internal use within the class or its subclasses. However, they can still be accessed from outside the class.
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
### Inheritance:
- Inheritance is a fundamental concept that allows a new class (subclass) to inherit attributes and methods from an existing class (superclass)> This facilitates code reuse and promote a herirachical structure among classes.

- Think of inheritance like a family tree, where a child inherit crtain traits, characteristics and behaviour from their parents. Similarly, in programming, a subclass inherits methods and attributes brom its superclass.

```
Syntax:

class Superclass:
    # Superclass definition

class Subclass(Superclass):
    # Subclass inherits from Superclass
    # Subclass-specific attributes and methods
```

## Types of Inheritance:

1. Single Inheritance:
- Single inheritance involves one subclass inheriting from one superclass. This is the most common type of inheritance.
```
Example:

class Animal:
    pass

class Dog(Animal):
    pass
```
2. Multiple Inheritance:
- Multiple inheritance involves one subclass inheriting from multiple superclasses. This allows a subclass to inherit attributes and methods from multiple sources.
```
Example:

class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass
```
3. Multilevel Inheritance:
- Multilevel inheritance involves a chain of inheritance where a subclass inherits from another subclass, creating a hierarchy.
```
Example:

class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass
```
4. Hierarchical Inheritance:
- Hierarchical inheritance involves multiple subclasses inheriting from a single superclass. This is also known as class hierarchy or class tree
```
Example:

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass
```
5. Hybrid (or Cyclic) Inheritance:
- Hybrid inheritance involves a combination of multiple types of inheritance. This can lead to complex inheritance structures.
```
Example:

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass
```


## Polymorphism
- Polymorphism is a fundamental concept in object-oriented programming that allows object of different classes to be treated as a object of a common super classes. It enables a single interface to represent the multiple types of objects and allow these objects to respond to the same message in different ways.
- Think of polymorphism like a remote control. Different devices (like TVs, sound systems, and DVD players) may have different implementations of the "power" button, but they all respond to the same command: "power on/off". Similarly, in programming, different objects may have different implementations of the same method, but they can all be called using the same interface


```
Example: 

class Animal:

    def speak(self):
        pass  # This will overridden by subclass

class Dog(Animal):
    def speak(self):
        sound = f"Sound of dog is 'Bark'"
        return sound
    
class Cat(Animal):
    def speak(self):
        sound = f"Sound of cat is 'Meow'"
        return sound
    

cat = Cat()
dog = Dog()

print(dog.speak())
print(cat.speak())
```

### Types of Polymorphism:
- There are two types of polymorphism:
1. Compile Time Polymorphism
2. Run Time Polymorphism

### 1. Compile-time Polymorphism
- It resolved during the compile-time
- It achived through types of overriding
- ### Types of Overloading in Python:-
- Method overloading : When a method has same name but different parameters.
- python does not support function or variable overloading, only method (or attribute) overloading is supported.



1. Method Overloading 
- Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The method in the subclass overrides the method in the superclass.
- When the name of a method is same but its functionality remains different for different types of arguments passed to it.
```
Example: 

class Animal:
    def speak(self):
        return "Animal speaks"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog()
cat = Cat()

print(dog.speak())  
print(cat.speak())  
```

2. Operator Overloading:
- Operator overloading : When we use an operator to operate on objects of user defined class.
- Operator overloading allows operators such as +, -, *, etc., to be redefined for objects of a class. This allows different operations to be performed depending on the operands and the context in which they are used.
- Operator overloading allows the creation of methods for operators such as +, -, *, / etc., which can be used with objects of a class Not directly supported by python, but we can achieve.
```
Example:

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    

a1 = Vector(2, 3)
a2 = Vector(4, 5)
a3 = a1 + a2

print(a3.y + a3.x)
```


### 1. Run-time Polymorphism
- Here polymorphism ressolved during the execution of program based on actual object at runtime.
- It is also known as Dynamic Binding or Late Binding.
- Run-time polymorphism achived through  method overriding and late binding.



## Abstraction:
- Abstraction is a fundamental concept in programming that involves hiding the complex implementation details of a system while exposing only the necessary functionality or interface to the users. It allows developers to focus on what an object does rather than how it does it.
  - Think of abstraction like driving a car. When you drive a car, you don't need to understand how the engine works or how the transmission system functions. Instead, you interact with the car using a simplified interface: the steering wheel, pedals, and gear shift. Similarly, in programming, abstraction allows you to interact with objects using their methods and attributes without needing to understand the internal implementation details.

```
Example:

class Car:

    def start(self):
        print("The car has started")

    def accellarate(self):
        print("The car is accellarating")

    def stop(self):
        print("The car has stopped")


# creating car object

my_car = Car()

# Intreract with car
my_car.start()
my_car.accellarate()
my_car.stop()
```

## Encapsulation 
- Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit called a class. It allows us to restrict access to certain components of an object, preventing direct modification of its internal state from outside the class.
- Encapsulation is achieved by defining attributes and methods within a class and controlling access to them using access modifiers like public, protected, and private. 

```
Example:

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
```