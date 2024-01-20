# ========================================================= LIST =========================================================

# List is a collection which is ordered and changeable. Allows duplicate members.

# Creating a List
my_list = ["Manish", "Yadhuvanshi", "Manish", 21, 854327]

# Access Items
# print(my_list) 
# print("This is the length of the list: ",len(my_list))
# print(my_list[3]) 
# print(my_list[0]) 
# print(my_list[0:2])

# Negative Indexing
# print(my_list[-1]) 
# print(my_list[-3]) 

# Checking if the element is present in the list:

# if "Manish" in my_list:
#     print("Yes")
# else:
#     print("No")

# Adding element in a list
    # There are three ways to add elements in a list:
        # 1. append()
        # 2. insert()
        # 3. extend()

my_list1 = [10,12,14,16,18,20]

# append()
my_list1.append(22)
# print(my_list1)

# insert()
my_list1.insert(1,"Number")
# print(my_list1)

# extend()
list3 = [30,31,32,33,34,35]
my_list1.extend(list3)
# print(my_list1)


# Removing elements from a list
    # There are three ways to remove elements from a list:
        # 1. remove()
        # 2. pop()
        # 3. del


# remove() 
list3.remove(35)
print(list3)

# pop()
list3.pop(2)
print(list3)

# del

list4 = [1,2,3,4,5]
list5 = [6,7,8,9,10]

list4.extend(list5)
print("This is extended list:")
print(list4)

# removing list using del function

del list4[2:5]
print("This is the list after deleting some elements:")
print(list4)

