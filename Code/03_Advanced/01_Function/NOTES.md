# FUNCTION

- A function is a block of reusable code that performs a specific task.
- Function helps organize the code, by making it more readable, modular, and easier to maintain.

## Syntax of Function:
![Function Syntax](https://github.com/iammanishk/Python-DSA/assets/101570741/e992b439-72ac-4651-913f-81cda82d3da7)


### Defining a Function:

- Use the function name followed by parentheses to call it.
- Function arguments are the values received by the function when it is invoked.

```
Example:

def greet(name):
    print("Hello", name, "Good Morning!")
    

name = input("Enter your name: ")
greet(name)
```
- In this example, `greet` is a function defined with one argument called `name`. When we run this program, it will ask for user's name and then display a message

### Return Statement:
- The return statement is used to exit a function and go back to the place from where it was called.
- The docstring ("""...""") provides a brief description of the function.

```
Example:

def sum(num1, num2):
    """This function adds two numbers"""
    ans = num1 + num2
    return ans

# WAP to find the sum of two numbers using function.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum is: ", sum(num1, num2))
```

### Positional Arguments:
- These are passed into functions based on their order in the function definition.

```
Example:

def details(name, age):
    """This function print details"""
    print(f"Name is: {name} and age is: {age}")
    return details

print(details(21, "Manish"))

# Ye name me '21' aur age me "Manish" ko add karega because of position.

```

### Keyword Arguments:
- When we call a function, we can use the name of the parameter to match the value to the parameter.
- Ye value ke name ko match karta hai.

```
Example:
def details(name, age):
    """This function print details"""
    print(f"Name is: {name} and age is: {age}")
    return details

print(details(name="Manish", age=21))

# Ye  name me "Manish" aur age me 21 ko add kara ga. Because yaha pe name aur age ke naam match kar rahe hai.
```


- We can provide default value for fuunction parameters, making them  optional. If no argument is provided while calling the function then the parameter will take its default value.

```
Example:

def sum (num1, num2 = 25):
    """This function adds two numbers"""
    ans = num1 + num2
    return ans


a = int(input("Enter first number: "))
print("Sum is: ", sum(a))
```

### Keyworded arguments or Arbitrary keyworded arguments(**kwargs):
- When you don't know that how many keyworded arguments will be passed to the function, then you can use **kwargs.
- `**kwargs` is used to pass variable number of keyworded arguments to a function
-  In `**kwargs` the arguments are passed as a `dictionary.`

```
Example:

def student_details(**kwargs):
    for x,y in kwargs.items():
        print(x, "is", y)

student_details(name="Manish", age=21, city="Purnea")
student_details(name="Anubhav", age=16, city="Jalalgarh")
```

### Nested Function:
- A nested function is a function within another function. The inner function can access all the variables from the outer function including its parameters and local variables.
- Nested function is used to avoid code redundancy and to improve code readability.

```
Example:

def outer(*args):
    i = int(input("Enter number: "))

    def inner(*args):
        x = int(input("Enter number: "))
        y = int(input("Enter number: "))
        sum = x + y+i
        return sum
    return inner()


output = outer()
print(output)
```

## Pass by value and Pass by reference

### Pass by value:
- In pass by value, a copy of an object is passed to the function. This means that any changes made to the object inside the function do not affect the original object.

```
Pass by value:

def addOne(x):
    x = x + 1
    print("Inside finction: ", x)

x = 5
addOne(x)
print("Outside function: ", x)
```

### Pass by reference:
- In pass by reference, a reference to the object is passed to the function. This means that any changes made to the object inside the function do affect the original object.

```
Pass by Reference:

def modified_list(list):
    list.append(4)
    print("Inside function: ", list)

list = [1,2,3]
modified_list(list)
print("Outside the function: ", list)
```

#### In python, all objeect are passed by object reference. This means that when you passing an object to a function, the function recive the reference to the object, not the object itself. If the function chage the object, the original object will also changed.

- #### Python uses pass by object reference, which is a combination of pass by value and pass by reference.

```
Pass by Object Referenc:

def modified_list(list):
    list.append(4)
    print("Inside function: ", list)

list = [1,2,3]
modified_list(list)
print("Outside the function: ", list)
```
