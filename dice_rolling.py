# loop 
# # ask: roll the dice
# If user wants to roll the dice, generate two random numbers between 1 and 6 and print them.
#  If the user does not want to roll the dice, print a thank you message. ternminate
#  If the user inputs an invalid choice, print an error message.

import random

while True:
    answer = input("Roll the dice? (y/n): ").strip()

    if answer.lower() == "y":
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        print(f"({num1}, {num2})")
    elif answer.lower() == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice")