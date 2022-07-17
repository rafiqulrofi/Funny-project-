import random

choice = ["rock", "paper", "scissors"]
computer = random.choice(choice)
player = None

while player not in choice:
    player = input("Your Choice is: ").lower()
print("Computer Choice is: ", computer)

if player == computer:
    print("It's Tie")
elif player == "rock":
    if computer == "scissors":
        print("You win!")
        print("Computer lose!")
    if computer == "paper":
        print("You lose")
        print("Computer win!")
elif player == "paper":
    if computer == "scissors":
        print("Computer win!")
        print("You lose!")
    if computer == "rock":
        print("You win")
        print("Computer lose!")
elif player == "scissors":
    if computer == "paper":
        print("You win!")
        print("Computer lose!")
    if computer == "rock":
        print("You lose")
        print("Computer win!")
