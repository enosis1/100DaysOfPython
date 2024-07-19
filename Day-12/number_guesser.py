import random
from os import system

import art


def check_guess(guess, number):
    """Checks the user guess to see if close to number or not."""
    if guess > number:
        print("You are too high! Guess again.")
    elif guess < number:
        print("You are too low! Guess again.")
    else:
        print(f"You guessed correctly! The number was {number}!")


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    EASY_DIFF = 10
    HARD_DIFF = 5
    if difficulty == "easy":
        return EASY_DIFF
    else:
        return HARD_DIFF


def game():
    """Plays the number game."""
    system("clear")
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)

    attempts = set_difficulty()

    while attempts > 0:
        guess = int(input("Guess a number: "))
        check_guess(guess, number)
        if guess == number:
            break
        else:
            attempts -= 1
            print(f"You have {attempts} attempts left.")

    if attempts == 0:
        print(f"The number was {number}.")


game()
