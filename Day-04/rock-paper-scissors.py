import random

rps_choices = ["rock", "paper", "scissors"]

user_choice = input("What do you choose? Type 'Rock', 'Paper' or 'Scissors' ").lower()
computer_choice = random.choice(rps_choices)

rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
if user_choice == "rock" and computer_choice == "rock":
    print("You chose rock!")
    print(rock_art)
    print("Computer chose rock!")
    print(rock_art)
    print("Tie game!")
elif user_choice == "rock" and computer_choice == "paper":
    print("You chose rock!")
    print(rock_art)
    print("Computer chose paper!")
    print(paper_art)
    print("You lose!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You chose rock!")
    print(rock_art)
    print("Computer chose scissors!")
    print(scissors_art)
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You chose paper!")
    print(paper_art)
    print("Computer chose rock!")
    print(rock_art)
    print("You win!")
elif user_choice == "paper" and computer_choice == "paper":
    print("You chose paper!")
    print(paper_art)
    print("Computer chose paper!")
    print(paper_art)
    print("Tie game!")
elif user_choice == "paper" and computer_choice == "scissors":
    print("You chose paper!")
    print(paper_art)
    print("Computer chose scissors!")
    print(scissors_art)
    print("You lose!")
elif user_choice == "scissors" and computer_choice == "rock":
    print("You chose scissors!")
    print(scissors_art)
    print("Computer chose rock!")
    print(rock_art)
    print("You lose!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You chose scissors!")
    print(scissors_art)
    print("Computer chose paper!")
    print(paper_art)
    print("You win!")
else:
    print("You choose scissors!")
    print(scissors_art)
    print("Computer choose scissors!")
    print(scissors_art)
    print("Tie game!")
