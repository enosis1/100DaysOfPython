############### Blackjack Project #####################

# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

import random
from os import system

import art


def deal_cards(cards, player_cards, computer_cards):
    """Deals one cards to the player and one card to the computer."""
    while len(player_cards) < 2:
        random_card = random.choice(cards)
        player_cards.append(random_card)

    while len(computer_cards) < 1:
        random_card = random.choice(cards)
        computer_cards.append(random_card)


def get_score(cards):
    """Returns the score of the current deck selected."""
    score = 0
    for card in cards:
        score += card

    return score


def check_for_ace(cards):
    """Checks to see if a player or computer's deck has an ace and changes the ace from 11 to 1."""
    new_cards = []
    for card in cards:
        if card == 11 and get_score(cards) > 21:
            card = 1
            new_cards.append(card)
        else:
            new_cards.append(card)
    return new_cards


def is_ace_in_deck(cards):
    """Returns a boolean value if there is an ace in a player or computer's deck."""
    for card in cards:
        if card == 11:
            return True


def add_new_card(player, cards):
    """Adds a new card to player or computer's cards."""
    random_card = random.choice(cards)
    player.append(random_card)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_game():
    while True:
        player_cards = []
        computer_cards = []
        game_playing = True

        is_play_blackjack = input(
            "Do you want to play a game of blackjack? Type 'y' for yes or 'n' for no.: "
        )

        if is_play_blackjack == "y":
            system("clear")
            print(art.logo)
        else:
            print("Exiting game...")
            break

        while game_playing:
            deal_cards(cards, player_cards, computer_cards)
            player_score = get_score(player_cards)
            computer_score = get_score(computer_cards)
            print(f"\tPlayers' cards: {player_cards}. Current score: {player_score}")
            print(f"\tComputer's first card: {computer_cards}")
            if player_score == 21:
                print(
                    f"\tPlayer Final Cards: {player_cards}. Final score: {player_score}"
                )
                print(f"\tComputer's final score: {computer_score}")
                print("You win with Blackjack!")
                game_playing = False
                break
            elif computer_score == 21:
                print(
                    f"\tPlayer Final Cards: {player_cards}. Final score: {player_score}"
                )
                print(f"\tComputer's final score: {computer_score}")
                print("You lose! Computer wins with Blackjack!")
                game_playing = False
                break

            if (
                player_score > 21
            ):  # If player cards are higher than 21 check if there is an ace
                if is_ace_in_deck(player_cards):
                    player_cards = check_for_ace(player_cards)
                    player_score = get_score(player_cards)
                    print("You have an ace!".center(30, "-"))
                    print(
                        f"\tPlayers' cards: {player_cards}. Current score: {player_score}"
                    )
                    print(f"\tComputer's first card: {computer_cards}")
                    if (
                        player_score > 21 and is_ace_in_deck
                    ):  # If there is an ace and player score higher than 21, lose
                        print(
                            f"\tPlayer Final Cards: {player_cards}. Final score: {player_score}"
                        )
                        print(f"\tComputer's first card: {computer_cards}")
                        print("You lose! Cards went over.")
                        game_playing = False
                        break
                else:
                    print(
                        f"\tPlayer Final Cards: {player_cards}. Final score: {player_score}"
                    )
                    print(f"\tComputer's first card: {computer_cards}")
                    print("You lose! Cards went over.")
                    game_playing = False
                    break

            new_card = input("Add a new card to your deck? 'y' or 'n': ")
            if new_card == "y":
                add_new_card(player_cards, cards)
                continue
            else:
                while computer_score < 17:
                    add_new_card(computer_cards, cards)
                    computer_score = get_score(computer_cards)
                if computer_score > 21:
                    print(
                        f"\tPlayer Final Cards: {player_cards}. Final score: {player_score}"
                    )
                    print(
                        f"\tComputer's cards: {computer_cards}. Computer score: {computer_score}"
                    )
                    print("You win! Opponent went over.")
                    game_playing = False
                    break
                elif computer_score == get_score(player_cards):
                    print(
                        f"\tPlayer Final Cards: {player_cards}. Final score: {player_score}"
                    )
                    print(
                        f"\tComputer's cards: {computer_cards}. Computer score: {computer_score}"
                    )
                    print(f"Draw, both cards ended up at: {player_score}")
                    game_playing = False
                    break
                elif computer_score > player_score:
                    print(
                        f"\tPlayer Final Cards: {player_cards}. Final score: {player_score}"
                    )
                    print(
                        f"\tComputer's final cards: {computer_cards}. Computer score: {computer_score}"
                    )
                    if computer_score == 21:
                        print("Computer wins with Blackjack!")
                    else:
                        print("Computer wins with a higher score.")
                    game_playing = False
                    break
                elif player_score > computer_score:
                    print(
                        f"\tPlayer Final Cards: {player_cards}. Final score: {player_score}"
                    )
                    print(
                        f"\tComputer's cards: {computer_cards}. Computer score: {computer_score}"
                    )
                    print("You win with a higher score.")
                    game_playing = False
                    break


play_game()
