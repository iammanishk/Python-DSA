# Write a program to check if all the elements in the list are unique. If the duplicate number is found exit the loop and print duplicate


list = ["Manish", "Yadhuvanshi", 21, 21, "Bihar"]
unique_item = set()

for i in list:
    if i in unique_item:
        print("Duplicate item found: ", i)
        break
    unique_item.add(i)
