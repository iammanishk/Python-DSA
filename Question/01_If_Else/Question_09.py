# Write a prpogram to accept percentage from the user and display the grade according to the following criteria:

# Marks                                     Grade
# More than 90                              A
# More than 80 and less then 90             B
# More than 60 and less then 80             C
# Below 60                                  D


# +++++++++++++++++++++++++++++++++++++++++++++++++ CODE +++++++++++++++++++++++++++++++++++++++++++++++++


percentage = int(input("Enter the percentage of the student: "))

if percentage > 90:
    print("The grade of the student is 'A'")
elif percentage > 80 and percentage <90:
    print("The grade of the student is 'B'")
elif percentage > 60 and percentage < 80:
    print("The grade of the student is 'C'")
else:
    print("The grade of the student is 'D'")
