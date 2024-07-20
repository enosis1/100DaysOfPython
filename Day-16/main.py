from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
money = MoneyMachine()


while True:
    order = input(f"What would you like? ({menu.get_items()}): ")

    if order == "report":
        coffee_machine.report()
        money.report()
        continue
    elif order == "off":
        print("Shutting down...")
        break
    elif menu.find_drink(order) is None:
        continue
    else:
        order = menu.find_drink(order)

    if coffee_machine.is_resource_sufficient(order):
        money.make_payment(order.cost)
        coffee_machine.make_coffee(order)
