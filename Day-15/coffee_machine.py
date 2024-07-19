from os import system

from menu import MENU, resources


def print_report():
    for resource, amount in resources.items():
        if resource == "water" or resource == "milk":
            print(f"{resource.capitalize()}: {amount}ml")
        if resource == "coffee":
            print(f"{resource.capitalize()}: {amount}g")
        if resource == "money":
            print(f"{resource.capitalize()}: ${float(amount)}")


def check_resources(drink_selected):
    """Returns True if order can be made, False if not."""
    for resource, resource_amount in resources.items():
        ingredientes = MENU[drink_selected]["ingredients"]
        if resource in ingredientes:
            if resource_amount < MENU[drink_selected]["ingredients"][resource]:
                print(
                    f"Sorry there is not enough {resource} to make the {drink_selected}."
                )
                return False
            return True


def process_coins():
    total = 0
    print("Please insert coins.")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    total += quarters + dimes + nickles + pennies
    return total


def process_change():
    change = 0
    user_money = process_coins()
    cost_of_drink = MENU[user_choice]["cost"]
    if user_money >= cost_of_drink:
        change += user_money - cost_of_drink
        print(f"Your change is ${round(change, 2)}.")
        return True
    else:
        print(f"That's not enough money for an {user_choice}.\nRefunding your coins...")
        return False


def make_coffee(coffee):
    """Makes a coffee and removes used ingredientes out of resources."""
    for ingredient in MENU[coffee]["ingredients"]:
        resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]


is_on = True

system("clear")

while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        is_on = False
        break
    if user_choice == "report":
        print_report()
        continue

    print(f"The {user_choice.capitalize()} cost {MENU[user_choice]["cost"]}.")
    if check_resources(user_choice):
        if process_change():
            resources["money"] = MENU[user_choice]["cost"]
            make_coffee(user_choice)
            print(f"Enjoy your {user_choice}!")
            continue
