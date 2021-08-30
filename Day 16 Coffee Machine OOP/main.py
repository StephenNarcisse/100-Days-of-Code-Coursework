from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
coffee_alpha = CoffeeMaker()
register_one = MoneyMachine()

machine_status = True

while machine_status:
    selection = input("What would you like to drink?: ")
    if selection == "report":
        coffee_alpha.report()
        register_one.report()
    elif selection == "off":
        machine_status = False
    else:
        drink = my_menu.find_drink(selection)
        if drink != "None":
            if coffee_alpha.is_resource_sufficient(drink):
                register_one.make_payment(drink.cost)
                coffee_alpha.make_coffee(drink)

