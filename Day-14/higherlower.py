import random
from os import system

import art
import game_data


def generate_person():
    """Generates a person from the list of data"""
    return random.choice(game_data.data)


def compare_people(person_a, person_b):
    comparison = input("Who has more followers? Type 'A' or 'B': ")
    comparison = comparison.lower()
    if comparison == "a":
        if person_a["follower_count"] > person_b["follower_count"]:
            return True
        else:
            return False
    elif comparison == "b":
        if person_b["follower_count"] > person_a["follower_count"]:
            return True
        else:
            return False


def format_person_name(person):
    """Format people's name in a format that is easily readable."""
    person_name = person["name"]
    person_desc = person["description"]
    person_location = person["country"]

    return f"{person_name}, {person_desc}, from {person_location}."


def game():
    """Start the Higher Lower Game."""
    person_a = generate_person()
    person_b = generate_person()
    while person_a == person_b:
        person_b = generate_person()
    score = 0

    while True:
        system("clear")
        print(art.logo)
        if score > 0:
            print(f"That was correct, your score is now {score}.")
        print(f"Compare A: {format_person_name(person_a)}")
        print(art.vs)
        print(f"Against B: {format_person_name(person_b)}")
        if compare_people(person_a, person_b):
            score += 1
            person_a = person_b
            person_b = generate_person()
            continue
        else:
            system("clear")
            print(art.logo)
            print(f"You lose! That was incorrect. Final Score: {score}")
            break


game()
