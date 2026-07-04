# genrate a random number between 1 to 100
# loop
# ask the user to guess the number
# if number is less than 0 or greater than 100, print "Invalid number. Please enter a number between 1 and 100."
# if number is less than the random number, print "Too low!"
# if number is greater than the random number, print "Too high!"
# when the user guesses the correct number, print "Congratulations! You guessed the number." and terminate the loop

import random

number = random.randint(1, 100)
while True:
    n = int(input("Guess a number between 1 and 100: "))
    if n < number:
        print("Too low!")
    elif n > number:
        print("Too high!")
    elif n < 1 or n > 100:
        print("Invalid number. Please enter a number between 1 and 100.")
    else:
        if n == number:
            print("Congratulations! You guessed the number.")
        break