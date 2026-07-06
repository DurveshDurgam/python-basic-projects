import random



while True:
    print("Welcome to Snake Water Gun Game!")
    user_choice = input("Enter your choice (snake, water, gun): ").strip().lower()
    choices = ["snake", "water", "gun"]
    computer_choice = random.choice(choices)


    if user_choice not in choices:
        print("Invalid choice! Please choose either 'snake', 'water', or 'gun'.")
    elif user_choice == computer_choice:
        print("It's a tie!")

    elif(user_choice == "snake" and computer_choice == "water") or \
    (user_choice == "water" and computer_choice == "gun") or \
    (user_choice == "gun" and computer_choice == "snake"):
        print(f"You win! {user_choice} beats {computer_choice}.")
    else:
        print(f"You lose! {computer_choice} beats {user_choice}.")

    print("Do you want to play again? (yes/no)")
    if input().strip().lower() != "yes":
        break
