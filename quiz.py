
response = input("Do you wanna play the Quiz? (y/n): ").lower().strip()

if response == "y":
    print("Great! Let's start the quiz.")
    q1 = input("What is the capital of France? ").lower().strip()
    if q1 == "paris":
        print("Correct!")
        count = 1
    else:  
        print("Incorrect. The correct answer is Paris.")

    q2 = input("What is 5 + 7? ").strip()
    if q2 == "12":
        print("Correct!")  
        count += 1
    else:
        print("Incorrect. The correct answer is 12.")

    q3 = input("What is the largest planet in our solar system? ").lower().strip()
    if q3 == "jupiter":
        print("Correct!")
        count += 1
    else:
        print("Incorrect. The correct answer is Jupiter.")

    q4 = input("What is the chemical symbol for water? ").lower().strip()
    if q4 == "h2o":
        print("Correct!")   
        count += 1
    else:
        print("Incorrect. The correct answer is H2O.")

    print(f"You got {count} out of 4 questions correct.")
    percent = (count / 4) * 100
    print(f"Your score is {percent:.2f}%.")
    
else:
    print("Maybe next time!")

