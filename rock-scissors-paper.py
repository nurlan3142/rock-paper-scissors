import random

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter rock, paper, or scissors (or 0 to stop): ").lower()

    if user_choice == "0":
        print("Game stopped")
        break

    if user_choice not in choices:
        print("Invalid input! Please write rock, paper, or scissors.\n")
        continue

    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It is a tie!\n")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!\n")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!\n")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!\n")
    else:
        print("Computer wins!\n")