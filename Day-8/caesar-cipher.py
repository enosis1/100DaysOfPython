import art

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(text, shift, direction):
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    if direction == "encode":
        encrypted_text = ""
        for letter in text:
            if letter in alphabet:
                letter_index = alphabet.index(letter)
                new_letter = alphabet[(letter_index + shift) % len(alphabet)]
                encrypted_text += new_letter
            else:
                encrypted_text += letter

        print(f"The encoded text is {encrypted_text}")

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    if direction == "decode":
        encrypted_text = ""
        for letter in text:
            if letter in alphabet:
                letter_index = alphabet.index(letter)
                new_letter = alphabet[(letter_index + shift) % len(alphabet)]
                encrypted_text += new_letter
            else:
                encrypted_text += letter

        print(f"The decoded text is {encrypted_text}")


print(art.logo)

user_continue = True

while user_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    user_exit = input("Do you wish to continue? Type 'y' for yes or 'n' for no: ")
    if user_exit == "n":
        user_continue = False
        print("Goodbye")
    else:
        continue
# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
