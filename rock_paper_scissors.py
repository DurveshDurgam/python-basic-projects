# Ask the user to make the choice.
# if choice is not in r, p or s print invalid choice. Please enter r, p, or s.
# print the choice
# let computer make a choice
# print the computer's choice
# compare the choices and print the result of the game.
# ask if wanna play again. If yes, repeat the game.
# if yes repeat, of no terminate the game
# print thanks for playing


import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

emojis = {
    "ROCK": "🪨",
    "PAPER": "📄",
    "SCISSORS": "✂️"
}
print("Welcome to Rock, Paper, Scissors!")
choices = ("ROCK", "PAPER", "SCISSORS")

def get_user_choice():
    while True:
        choice = input("Enter your choice (ROCK, PAPER, SCISSORS): ").strip().lower()
        if choice in choices:
            return choice
        else:
            print("Invalid choice. Please enter ROCK, PAPER, or SCISSORS.")

def display_choices(user_choice, computer_choice):
    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "ROCK" and computer_choice == "SCISSORS") or 
        (user_choice == "PAPER" and computer_choice == "ROCK") or 
        (user_choice == "SCISSORS" and computer_choice == "PAPER")):
        return "user wins"
    else:
        return "computer wins"

def game():
    while True:
        choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(choice, computer_choice)

        result = determine_winner(choice, computer_choice)
        print(f"Result: {result}")

        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            break

game()
print("Thanks for playing!")