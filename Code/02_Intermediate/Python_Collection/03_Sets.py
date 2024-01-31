# ========================================================= SETS =========================================================


#  A set is an unordered collection of unique elements. The primary characteristics of sets are that they do not allow duplicate values, and the order in which elements are stored is not guaranteed. Sets are defined by enclosing elements within curly braces {} or by using the set() constructor.




# ----------------------------------- Creating a Set -----------------------------------

set = {"Manish", 21, 854327}
print(set)
# print(len(set))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> OPERATIONS ON SETS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Addition of elements to the set using "|" operator.
set1 = {1, 2, 3}        
set2 = {4, 5, 6, 3}
set3 = set1 | set2
# print(set3)

# Addition of elements to the set using "update()" function.

set1.update(["Number", "Set"]) # We can add multiple elements using update() function.

set2.add(7) # We can add only one element using add() function.

set1.update(set2)
print(set1)


















# ----------------------------------- Accessing Elements -----------------------------------

# We cannot access elements in a set by referring to an index, since sets are unordered the elements has no index. But we can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the "in" keyword.


# Checking that an element is present in the set or not.

if "Manish" in set:
    print("Yes Manish is in the set")
else:
    print("No Manish is not in the set")