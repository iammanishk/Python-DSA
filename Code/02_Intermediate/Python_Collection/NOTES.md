# Collections
#### In pyhton **collection**  are refers to data structure or container that are used to store and organize multiple value.
### Pyhton provides severals built-in collection types :
1. List
2. Tuples
3. Sets
4. Dictionaries

# List
#### A list is built-in data-structure of pyhton that store an ordered collection of elements.
### List are muitable that means, you can modify their content by adding, removing or changing the element. And it can have duplicate element
### List contains data of different types of datatype, and they are defined by enclosing the element by square brackets(`[]`), and seperated by comma.

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

- ## del() delets the more than one element in list

```
example of del();

del new_list1[1:3]
print(new_list1)
# ye first index se second index (3-1) tak delet krta hai
```
