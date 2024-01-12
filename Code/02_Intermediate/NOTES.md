# CONDITIONAL OPERATORS
#### conditional operators are used to make decisions in your code based on certain conditions. These operators are typically used in conjunction with control flow statements like if, elif (else if), and else

- if, if-else
- nested
- else if ladder
- ternary
- switch

## 1. if statement:
#### The if statement is used to execute a block of code only if a specified condition is true.
  ```
   x = 10

   if x > 5:
       print("x is greater than 5")
  ```

## 2. if-else statement:
#### The if-else statement extends the if statement by providing an alternative block of code to be executed when the condition is false.
```
x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```
## 3. elif statement:
#### The elif (else if) statement is used to check additional conditions if the preceding if or elif conditions are false.
```
x = 5

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

```

### You can have multiple elif statements to check multiple conditions.
```
grade = 75

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
```

## Match Case
#### Match case simplifies the use of if and elif chains, especially when dealing with nested structures like lists, tuples, and dictionaries.
#### This is also known as **Pattern Matching**
#### If you are familiar with C and C++ than you will know it by Switch statement

- ### This is introuduced in **PYTHON** `V3.10`

```
def check_value(value):
    match value:
        case 0:
            print("It's zero")
        case 1 | 2:
            print("It's either 1 or 2")
        case int() if int() > 2:
            print("It's an integer greater than 2")
        case str(s):
            print(f"It's a string: {s}")
        case _:
            print("It doesn't match any of the above")


eg.(check_value(1))
```