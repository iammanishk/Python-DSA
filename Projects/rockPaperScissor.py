# ---------------------------- Rock Paper Scissor game   (easy level) ----------------------------
import random


option = ["rock", "paper", "scissor"]

print(f"Welocme to the Rock Paper Scissor game")

userWins = 0
computerWins = 0

while True:
    userInput = input(f"Enter Rock/ Paper/ Scissor or Q for Quit: ").lower()

    if userInput == "q":
        print("Bye Bye👋")
        quit()

    if userInput not in option:
        continue

    randomNumber = random.randint(0, 2)  # 0 for rock, 1 for paper, 2 for scissor
    computerPicks = option[randomNumber]  # computer picks random option
    print(f"computer picks: {computerPicks}")

    if userInput == "rock" and computerPicks == "paper":
        print(f"You win")
        userWins += 1
    elif userInput == "scissor" and computerPicks == "paper":
        print(f"You win")
        userWins += 1
    elif userInput == "paper" and computerPicks == "rock":
        print(f"You win")
        userWins += 1
    else:
        print(f"Computer wins")
        computerWins += 1

    print(f"Your score: {userWins} \nComputer score: {computerWins}\n\n")

