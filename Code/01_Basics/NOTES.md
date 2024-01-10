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