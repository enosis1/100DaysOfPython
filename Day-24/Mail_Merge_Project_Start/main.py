# TODO: Create a letter using starting_letter.txt
names = []

with open("./Input/Names/invited_names.txt", "r") as file:
    contents = file.readlines()
    for name in contents:
        names.append(name.replace("\n", ""))

with open("./Input/Letters/starting_letter.txt", "r") as file:
    letter = file.read()
    print(letter)

for name in names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        new_contents = letter.replace("[name]", name)
        file.write(new_contents)

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
