# --------------------------------------------------------  ARRAY  --------------------------------------------------------
from array import *
# Syntex of array:-
# variable_name = array(typecode,[elements])

# Examples:-

age = array('i', [12,13,8,45])
print(age)

for x in age:
    print(x)

# Array methods:-
    
# append() :- Adds an element at the end of the array
age.append(10)
print(age)

# insert() :- Inserts an element at the specified position
age.insert(2, 20)
print(age)

# pop() :- Removes the element at the specified position and returns it's value
age.pop  # remove last element
age.pop(2)  # remove element at index 2
print(age)

# remove() :- Removes the first occurrence of the element with the specified value
age.remove(13)
print(age)

# reverse() :- Reverses the order
age.reverse()
print(age)

# index() :- Returns the index of the first occurrence of the element with the specified value
print(age.index(8))

# count() :- Returns the number of elements with the specified value
print(age.count(8))

# extend() :- Add the elements of a list (or any iterable), to the end of the current array
age.extend([5,6,7])
print(age)

# tolist :- Convert array to list
print(age.tolist())