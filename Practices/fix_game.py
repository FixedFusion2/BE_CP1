# TE 2nd Fix Game
import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: "))# Logic Error, needs integer.
        attempts = attempts +1 #While loop needs 10 attepts
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the number!")# needs to become leif because its independent adn will still run code after, Logic Error.
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  
        continue# Redundent
    print("Game Over. Thanks for playing!")
start_game()