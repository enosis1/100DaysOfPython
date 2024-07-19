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


def check_resources(drink_selected, resources):
    for item, item_amount in resources.items():
        if item in MENU[drink_selected]["ingredients"]:
            if item_amount > MENU[drink_selected]["ingredients"]["water"]:
                print(f"We have {item_amount} of {item} to make {drink_selected}")
                return True
            else:
                print(
                    f"We do not enough {item} to make {drink_selected}. {item} amount is at {item_amount}."
                )
                return False


is_on = True

system("clear")
check_resources("espresso", resources)

while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        is_on = False
        break
    if user_choice == "report":
        print_report()
        continue
