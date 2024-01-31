# ========================================================= SETS =========================================================


#  A set is an unordered collection of unique elements. The primary characteristics of sets are that they do not allow duplicate values, and the order in which elements are stored is not guaranteed. Sets are defined by enclosing elements within curly braces {} or by using the set() constructor.




# ----------------------------------- Creating a Set -----------------------------------

set = {"Manish", 21, 854327}
print(set)
print(len(set))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> OPERATIONS ON SETS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Addition of elements to the set using union "|" operator.
set1 = {1, 2, 3}        
set2 = {4, 5, 6, 3}
set3 = set1 | set2
print(set3)


# Intersection (&):
# This returns a set, that contains only the elements that are common to all the sets.

insersection_set = set1 & set2
print("This is insersection set: ",insersection_set)



# Difference (-):
# This returns a new set containing elements present in the first set but not in the second.

difference_set = set1 - set2
print("This is difference set: ",difference_set)


# Symmetric Difference (^):
# Returns a new set containing elements that are unique to each set.

symmmetric_set = set1 ^ set2
print("This is symmetric set: ",symmmetric_set)

# Addition of elements to the set using "update()" function.

set1.update(["Number", "Set"]) # We can add multiple elements using update() function.

set2.add(7) # We can add only one element using add() function.

set1.update(set2)
print(set1) 


# ----------------------------------- Removing Elements -----------------------------------
# Removing an element using remove() method:
set1.remove(12)
print(set1)

# Removing an element using discard() method:
set1.discard(12)
print(set1)

# Removing an element using pop() method:
#  It removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.

pop_set = set1.pop()
print("pop set: ",set1)

# ----------------------------------- Checking Elements -----------------------------------

# Checking that an element is present in the set or not.

# if "Manish" in set:
#     print("Yes Manish is in the set")
# else:
#     print("No Manish is not in the set")