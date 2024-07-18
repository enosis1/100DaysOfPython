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
        print("You guessed correctly!")


system("clear")
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 0
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5


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
