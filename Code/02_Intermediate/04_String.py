
name = "   ManIsh Yadhuvanshi"

first_char = name[0]
print("First character is: ", first_char)

first_name = name[0:6]
print("First name is: ", first_name)

print(name.upper())
print(name.lower())
print(name.title())
print(name.strip()) # removes the leading and trailing spaces
print(name.replace("Yadhuvanshi", "Kumar"))


fruit = "apple, banana, orange, pomigranate, mango, guava, kiwi, grapes, watermelon"
print(fruit.split()) # split the string into list of strings based on space delimiter
print(fruit.split(", ")) # split the string into list of strings based on comma and space
print(fruit.find("banana")) # find the index of the substring in the given string
print(fruit.find("mango")) # find the index of the substring in the given string
print(fruit.count("mango")) # count the number of occurences of the substring in the given string

chai_type = "masala"
quantity = 2
order = "I want {} cups of {} chai"
print(order.format(quantity, chai_type)) # format the string with the given values


chai = ["masala", "adrak", "elaichi", "kali mirch", "kashmiri"]
print("".join(chai)) # join the list of strings into a single string using empty separator
print(", ".join(chai)) # join the list of strings into a single string using comma and space separator

path = r"C:\Users\Manish\Desktop\Python\Code\02_Intermediate\04_String.py" # raw string to avoid escape characters
print(path)



# ---------------------------------------------------------- SLICING ----------------------------------------------------------

my_list = "0123456789"
print(my_list[:])
print(my_list[0:])
print(my_list[:2])
print(my_list[4:])
print(my_list[0:7:2]) # hopping of 2
print(my_list[0:7:3]) # hopping of 3
