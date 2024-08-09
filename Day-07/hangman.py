# Step 4

import random

import hangman_ascii
import hangman_words

stages = hangman_ascii.stages
word_list = hangman_words.word_list
logo = hangman_ascii.logo

random_word = random.choice(word_list)
word_length = len(random_word)

lives = 6

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

end_of_game = False
print(logo)
print()
print(f"The word is {random_word}.")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed the letter '{guess}'.")

    for position in range(word_length):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in random_word:
        print(f"Letter {guess} is not in the word! You have lost a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
