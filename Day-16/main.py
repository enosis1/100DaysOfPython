from os import system

from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

is_on = True
system("clear")
while is_on:
    order = input(f"What would you like? ({menu.get_items()}): ").lower()

    if order == "off":
        print("Exiting...")
        is_on = False
    elif order == "report":
        coffee_machine.report()
        money.report()
    else:
        drink = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink) and money.make_payment(
            drink.cost
        ):
            coffee_machine.make_coffee(drink)
