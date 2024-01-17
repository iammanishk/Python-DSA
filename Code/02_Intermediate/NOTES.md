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
## Ternary Operator
#### The ternary operator is a concise way to express a conditional statement. It is sometimes referred to as the "conditional expression" or "ternary expression." 

```
num = int(input("Enter any number: "))

output = "Even" if num % 2 == 0 else "odd"
print("Output is", output)
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

<hr>
<br><br>

# Loops
#### Loops in pyhton is somthing doing a task repeatidely until a particular condition is satisfied.
- There are two types of loops in python - `for loop` & `while loop`.

## FOR LOOP
#### The for loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each element in the sequence.
#### _For loop is like maine tumhe 10 rupee diye hai tum 10 ghanta kaam karo (1 rupee ke badle ek ghanta , to 10 rupee ke badle 10 ghanta)_

```
example:
for i in rupee 10:
    print(kaam kro)
```

```
# Example of a for loop with a list

fruits = ["apple", "orange", "banana"]
for i    in fruits:
    print(fruit)
```

- The range() function is often used in for loops to generate a sequence of numbers.

```
# Example of a for loop with range

for i in range(1, 10):
    print(i, ": Jay Shree Ram ")
```

## while Loop:
#### The while loop is used to repeatedly execute a block of code as long as a specified condition is true.

#### _While loop is like maine tumhe 10 rupee diye hai na, jab tak 10 rupee khatam nahi ho jaata tab tak kaam karo_

```
# Example of a while loop

count = 0
while count < 5:
    print(count)
    count += 1
```

- ## Both for and while loops can be controlled using loop control statements:

### Continue statement: Skips the rest of the code inside the loop for the current iteration and proceeds to the next iteration.
#### _Contiue statement be like meri chinta mat karo tum aage badho next iteration ko pakdo._
 ```
 for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
 ```

 ### Break statement: Terminates the loop prematurely, and the control is transferred to the next statement after the loop.

 #### _Break statement be like main tumhara raja hun main agar mar jaun to tum yahi se laut jaana next iteratrion ko kabhi mat pakadna_
 ```
 for i in range(10):
    if i == 5:
        break
    print(i)
 ```