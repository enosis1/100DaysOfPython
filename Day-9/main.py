import os

import art

os.system("clear")
print(art.logo)
print("Welcome to the blind auction.")

active_flag = True

active_bidders = {}


def add_to_dictionary(user, bid, dictionary):
    dictionary[user] = bid


def get_highest_bidder(dictionary):
    highest_bidder = ""
    highest_bid = 0
    for user, bid in dictionary.items():
        if bid > highest_bid:
            highest_bidder = user
            highest_bid = bid
    os.system("clear")
    print(f"The highest bidder was {highest_bidder} with a bid of ${highest_bid}.")


while active_flag:
    user = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))  # Logan was here
    add_to_dictionary(user, bid, active_bidders)
    is_exit = input(
        "Are there any other bidders? Type 'yes' to continue or 'no' to exit. "
    )
    if is_exit == "no":
        active_flag = False
    else:
        os.system("clear")

get_highest_bidder(active_bidders)
