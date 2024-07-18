print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")  # What is your name?
name2 = input("What is their name? ")  # What is their name?

name1 = name1.lower()
name2 = name2.lower()
both_names = f"{name1} {name2}"

true_total_count = 0
love_total_count = 0

true_total_count += both_names.count("t")
true_total_count += both_names.count("r")
true_total_count += both_names.count("u")
true_total_count += both_names.count("e")
love_total_count += both_names.count("l")
love_total_count += both_names.count("o")
love_total_count += both_names.count("v")
love_total_count += both_names.count("e")

true_string = str(true_total_count)
love_string = str(love_total_count)

score = f"{true_string}{love_string}"
score = int(score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f"Your score is {score}.")
