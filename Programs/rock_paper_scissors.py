import random


def rock_paper_scissors():
    print("\nRock-Paper-Scissors Game")
    choices = ["rock", "paper", "scissors"]
    user_score, computer_score = 0, 0

    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'exit' to quit): ").lower()
        if user_choice == "exit":
            break

        if user_choice not in choices:
            print("Invalid choice. Try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")

rock_paper_scissors()