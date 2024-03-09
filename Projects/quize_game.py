# Simple quize gmae using if else (easy level)


print("Welcome to the quize game")
playing = input(f"Do you want to play?\n'Yes' or 'No':  ").lower()

if playing != "yes":
    quit()
else:
    print("Let's play!")

score = 0
print(f"Okay, I will ask you 10 questions. \nYou have to answer them correctly.\n")

print(f"Question 1:  What is the capital city of Australia?")
answer = input("A. Sydney\nB. Melbourne\nC. Canberra\n").lower()

if answer == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"Question 2:  Who wrote the play Romeo and Juliet?")
answer = input("A. Jack Ma\nB. William Shakespeare\nC. Ram Naresh\n").lower()

if answer == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print(f"Question 3:  What is the largest planet in our solar system?")
answer = input("A. Earth\nB. Jupiter\nC. Mars\n").lower()

if answer == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print(f"Your score is {str(score)} out of 3.  \nThank you for playing!")
