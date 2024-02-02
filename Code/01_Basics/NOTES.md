# NOTES OF THE BASICS 

## ```print``` is used for print any things
```
print("Jay Shree Ram")
```

## ```Variables``` are just like container that stores something like **data**, and container in the sense *memory*.

```
x = 5
y = -1
name = "Manish"
login = "true"
```

### Formatted string literals:
-  It also allows you to embed expressions inside the string using curly braces {}.

```
Example:

name = input("Enter your name: )
print(f"Hello {name} How are you")
```


### And data could be anything
- It could be Integers
- It couold be String
- It could be Number and many more

**Naming Rule For Vailable**
- A variable name must start with a letter or with underscore
- A variable name cannot start with number
- A variable name can only start with Alphanumberic and Underscore (A-z,0-9 and _ )
- A variabe name case-sensitive (name, Name and NAME are different)
- A variable name cannot be any Python *keyword*

> In Python there are some reserved word which is called *Keyword*

## ```DataTypes``` are classifications that specify which type of value a variable can hold.The interpreter uses these *datatypes* to understand how to manipulate and store data in the memory.

### 1. int : Integers datatype represent the whole numbers (eg. 8, -48)
### 2. float : Floating-point datatype represent the decimal number (eg. 3.58, -4.85)
### 3. str : String type, represintingsequence of character ( eg. "Manish", "yadhuvanshi')
### 4. list : List type, represinting ordered and mutable sequences ( eg. [1,2,3])
### 5. tuple : Tuple type, represinting ordered and immutable sequences ( eg. (1,2,3))
### 6. set : Set type, representing the unordered collection of unique elements ( eg. {1,2,3})
### 7. dict : Dictionary type, representing the key-value pairs ( eg. {"key": "value"}, {"name":"Manish", "age': 20}, here name is *key* and manish is *value*)
### 8. bool: Boolean type, representing either True or False. (eg. "login = True")
### 9. none : NoneType represents the absence of a value or a null value. (eg. "valur = none)
### 10. complex_num : Complex dataType is used to represent the complex number. A complex number is somthing that comprise both *real part* and the *imaginary part*. (eg. complex_num = 3 + 2j)

* You can check the datatypes by:
```
print(type(variableName)) 
```
* You cha check the ascii value by usin ```ord function```
```
char = "M"
print(ord(char)) # this will gives you the ascii value of M
```
* You can check the value corsponding to the ascii value by usin ```chr function```
```
ascii = 64
print(chr(ascii)) # output of this is '@'
```
<hr>

## `input` is used to get any value froom the user
```
name = input("What is your name? ") 
# this will take your name and stores it into the name variable

print("Hello " + name) 
# this will print your name by adding prifix Hello
```
### - Note : input always take string, means if you are givin the input *int value* input treat with that as a string. Then we use at that place `typecasting`.

### `typecasting` is used to convert one datatype into another

```
name = input("What is your name? ")
  # this will sotre string value
rollNo = int(input("Enter your roll number! )) 
  # but this will store an int value
```
<hr>

## OPERATORS
#### Operators in python are symbols that perform operations on variables when they appear together in an expression

1. Arithmetic Operators:

- `+` : Addition
- `-` : Subtraction
- `*` : Multipication
- `/` : Division
- `%` : Modulus i.e., remainder after division
- `//` : Floor Division - result is the quotient rounded down to the nearest integer
- `**` : Exponentiation

    ```
    a = 10
    b = 3

    sum_result = a + b       # 13
    difference_result = a - b  # 7
    product_result = a * b    # 30
    division_result = a / b   # 3.333...
    remainder_result = a % b  # 1
    floor_division_result = a // b  # 3
    exponentiation_result = a ** b  # 1000
    ```

2. Comparison Operators:

- `==` : Equal to
- `!=` : Not equal to
- `<` : Less than
- `>` : Greater than
- `<=` : Less than equal to
- `>=` : Greater than equal to

    ```
    x = 5
    y = 10

    is_equal = x == y        # False
    not_equal = x != y       # True
    less_than = x < y        # True
    greater_than = x > y     # False
    less_than_equal = x <= y  # True
    greater_than_equal = x >= y  # False
    ```

3. Logical Operators:
   - and (Logical AND)  Return true is both statement are true
   - or (Logical OR)    Return true if one of the statement are true
   - not (Logical NOT)  Reverse the result, return false if the result is true

   ```
    p = True
    q = False
    logical_and = p and q     # False
    logical_or = p or q       # True
    logical_not = not p       # False

   ```

## *Note* : Rest are updating soon