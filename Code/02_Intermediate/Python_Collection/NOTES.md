# Collections
#### In pyhton **collection**  are refers to data structure or container that are used to store and organize multiple value.
### Pyhton provides severals built-in collection types :
1. List
2. Tuples
3. Sets
4. Dictionaries

# List
#### A list is built-in data-structure of pyhton that store an ordered collection of elements.
- List are muitable that means, you can modify their content by adding, removing or changing the element. And it can have duplicate element
- List contains data of different types of datatype, and they are defined by enclosing the element by square brackets(`[]`), and seperated by comma.

```
example of list :

list = ["Manish", "kumar", 21, 854327]
print(list)
```

## *There are three ways to add elements in a list*
1. append()
2. insert()
3. extend()

- ### Append add item to the end in a list
```
example of append():

list.append("Bihar")
print(list)
```


- ### Insert add element at any place by using index
```
example of insert():

list.insert(2,"Male")
print(list)
```

- ### Extend is used to add another list in the current list
```
example of extend():

new_list = ["BCA", "MMDU"]
list.extend(new_list)
print(list)
```


## *There are three ways to remove an element from a list*
1. remove()
2. pop()
3. del()

```
new_list1 = [1,2,3,4,5]
new_list2 = [6,7,8,9,10]
```
- ### remove() deletes the element by giving exactely value
```
example of remove():

new_list2.remove(10)
print(new_list2)
```

- ### pop() deletes an element by using index of the element
```
example of pop():

new_list2.pop(2)
print(new_list2)
```

- ### del() delets the more than one element in list

```
example of del();

del new_list1[1:3]
print(new_list1)
# ye first index se second index (3-1=2) tak delet krta hai
```


## *There are two ways to updating any list*
1. At an index
2. Range of index

- ### At an index : You can update a list of any particular index
```
example of at an index:

new_list1[1] = 200
print(new_list1)
```

- ### Range of index : You can update multiple items of a list
```
example of range of list:

new_list2[0:3] = [600, 700, 800]
```
- Note that we have used `:` for showing the range and `[ ]` is used for giving

- Since we changing the multiple elements so that we give the new value in a list form. `[600, 700, 800]`



## _LIST COMPERENSION_
#### In pyhton **List Comprehension** is a concise and expressive way to create a list. It allow you to generate a new list by applying an expression to each item in an existing iterable and optioinally including a condition to filter elements.

- List comprehension me aap new list create kar skte hain kisi bhi pehle se bana hua list se aur usme aap conditions bhi lga skte hain (jaise mujhe sirf even number hi chahiye, etc).

```
List Compherension example:

lc= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
new_lc = [i for i in lc if i%2==0]
print(new_lc)
```

## _NESTED LIST_
- In pyhton you can also make a list into another list which is called **nested list**.

```
Nested List example:

nL = ["Manish", "Yadhuvanshi", [21,854327, +914561237779], "Bihar", "India"]
new_nL = nL[2]
print(new_nL)
```

# TUPLES
#### Tuples are similar to lists but they are immutable means once you assign a value to it you cannot change or modify that value again.
- Tuples are defined by enclosing elements within parentheses  `( )`, separated by commas. 

- Tuples are faster than lists because of static in nature. They do not support changes to their size, and they cannot be changed after creation.

```
Example:

tup = (12,07,"Manish")
print(tup)
```

- They can contain any type of objects, including other tuples.
```
Nested Tuple:

nested_tup = (12, 0.7, ("Manish", "Yadhuvanshi"), (854327, "BCA", ("C++", "Python")) )

print(nested_tup)
```

### Creating a tuple with single element:
- You can create a tuple with single element by putting a comma `,` after the element. This is called a singleton tuple.

```
Example of Singleton:

single_Tup = ("Manish") # This is not a tuple 
print(type(single_Tup))

single_Tup = ("Manish",) # This is a Single element tuple
print(type(single_Tup))
```


### Accessing elements of a tuple
- You can access tuple elements by referring to the index number, inside square brackets `[]`.

```
Accessing element: 

print("Accessing elements using Index: ", tup[2])
print("Accessing element form backword: ",tup[-1])

print("Accessing element from nested tuple:", nested_tup[3][2][1])
print("Accessing element by using range index:", nested_tup[1:4])
```

###  Checking if an element exists in tuple:

```
if "BCA" in nested_tup[3]:
    print("Yes, 'BCA' is in the tuple")
else:
    print("No, 'BCA' is not in the tuple")
```

### Changing a Tuple:
- Unlike lists, tuples are immutable. This means that elements of a tuple cannot be changed once they have been assigned. But, if the element is itself a mutable data type like list, its nested items can be changed.

```
Changing a Tuple:

tuple_list = list(tup)
tuple_list[2] = "Yadhuvanshi"
tup = tuple(tuple_list)
print("Tuple after changing value : ", tup)
```


### Tuple Packing and Unpacking:
- Tuple packing involves putting multiple values in a tuple, and tuple unpacking involves extracting the values back into variables.

```
Unpacking a Tuple:

tup1 = ("Manish", 854327, "BCA")
name, pin, course = tup1
print(pin)
print(course)
print(name)
```


### Slicing of Tuple:
```
Example of Slicing:

fruit = ("Apple", "Banana", "Cherry", "Orange", "Kiwi", "Melon", "Mango")

first_three_fruit = fruit[0:3]
print(first_three_fruit)
print(len(first_three_fruit))
```


# SETS:
- A set is an unordered collection data type that is iterable, mutable, and has no duplicate elements.
- It supports membership test operations (in), search for an element with the help of in keyword.
- Set objects also support set arithmetic operations like union, intersection, difference, symmetric difference.
- Sets are defined by enclosing element within curly braces `{}` or by usiung the `set()` constructor.  

```
Example:

set = {"Manish", 21, 854327}
print(set)
```


## SET OPERATION

### Adding elements:

1. Addition of elements to the set using "update()" function.
- We can add multiple elements using update() function.(eg. list, tuple)


```
update function():

set1 = {1, 2, 3}  
set1.update(["Number", "String"])
print(set1)
```

2. Addition of element to the set using "add()" function.
-  We can add only one element using add() function.

```
add function():

set1.add(8)
print(set1)
```

3. Adding two sets together using union `|` operator:
- This  will not remove any common elements from both sets but it will combine all unique elements present in both sets.
- Returns a new set containing all unique elements from both sets.

```
Example:

set1 = {1, 2, 3}        
set2 = {4, 5, 6, 3}
set3 = set1 | set2
print(set3)
```

4. Intersection (&) Method:
- This returns a set, that contains only the elements that are common to all the sets

```
Example:

insersection_set = set1 & set2
print("This is insersection set: ",insersection_set)
```

5. Difference (-):
- This returns a new set containing elements present in the first set but not in the second.

```
Example:

difference_set = set1 - set2
print("This is difference set: ",difference_set)
```

6. Symmetric Difference (^):
- Returns a new set containing elements that are unique to each set.

```
Example:

symmmetric_set = set1 ^ set2
print("This is symmetric set: ",symmmetric_set)
```

### Removing Elements:

1. remove() method:
- It removes an element from the set if it exists. If the value is not found in the set, then it gives you the KeyError

```
Example:

set1.remove(12)
print(set1)
```

2. discard() method:
-  It also removes an element from the set, but unlike remove(), it doesn’t raise an error if the specified value is not found.

```
Example:

set1.discard(12)
print(set1)
```



# DICTIONARY:
- A dictionary is a data structure that allows you to store and retrieve values using a key.
- It is similar to a real-world dictionary where you look up words to find their meanings.
- In a Python dictionary, each key is associated with a value, forming a key-value pair.

```
Example:

student = {
    'name' : "Manish Yadhuvanshi",
    'age' : 21,
    'courses' : ["Python", "Machine Learning", "Data Science"],
    'is_active' : True
    }

print(student)
```

- Because dictionary is key value-pair, so here `key` is ''name'' and `value` is "Manish Yadhuvanshi"

- You can also access their  values by referring the `key`.

```
Example: 

print("Name of student: ", student['name'])
print("Age of student: ", student['age'])
```


- Dictionary items could be **Ordered** and **Changable**
- In dictionary duplicate value is not allowed and it
- In dictionary you can add any **datatype**
```
List datatypes example:

'courses' : ["Python", "Machine Learning", "Data Science"],
```

### Accessing the dictionary:
- You can access the items of a dictionary by referring to its key name, inside square brackets `[]`. If the item is not found, it will raise a KeyError.

```
Example:

print("Name of student: ", student['name'])  # This will print correctly
print("Age of student: ", student['village'])  # This will gives KeyError
```

- If you try to access a key that doesn’t exist in the dictionary, Python will raise an error.
- To avoid this we use `get()` method which returns 'None' if the key does not exist in the dictionary.

```
Example:

print("Phone number of student: ", student.get('village'))  # This will not gives error insted of that it gives 'None'
```

### Modifying Values:
- You can change the value of a specific item by referring to its key name.

```
Example:

student['age'] = 20
print(student)
```

### Adding New Key-Value Pairs:
- Adding an item to the dictionary is done by using a new index key and assigning a value to it.

```
Example:

student['email'] = "iammaanisshhh@gmail.com"
student['grade'] = "A+"
print(student)
```

- You can also use update() method to add new key-value pairs to the dictionary

```
Example:

address = {
    'city' : "Purnea",
    'state' : "Bihar",
    'country' : "India"
}

student.update(address)
print(student)
```

### Removing Key-Value Pairs:

- Removing an item from the dictionary is done by using the pop() method. This method removes the item with the specified key name.

```
Example:

student.pop('grade') # This removes the whole pair (key & Value).
# print(student)
```

- The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead).

```
Example:

student.popitem()
print(student)
```

- You can remove the key-value pair using del keyword also.

```
Example:

del student['email']
print(student)
```

### Checking if the item is present in the dictionary or not:
- To determine if a specified key is present in a dictionary use the 'in' keyword

```
Example:

if 'age' in student:
    print("Yes, 'age' is one of the keys in the student dictionary")
else:
    print("No, 'age' is not any of the keys in the student dictionary")
```