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