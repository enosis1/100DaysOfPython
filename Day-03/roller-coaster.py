print("Welcome to the rollercoaster!")
height = int(input("How tall are you? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    bill = 0

    if age < 12:
        print("You must pay $5.")
        bill += 5
    elif age >= 12 and age <= 18:
        print("You must pay $7.")
        bill += 7
    else:
        print("You must pay $12.")
        bill += 12

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or wants_photo == "y":
        bill += 3
    print(f"Your total bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
