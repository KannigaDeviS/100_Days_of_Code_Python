from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
TurnOn = True
while TurnOn:
    choice = input(f"What would you like? ({menu.get_items().rstrip('/')}): ")
    if choice == 'off':
        TurnOn = False
    elif choice == 'report':
        coffeeMaker.report()
    else:
        drink = menu.find_drink(choice)
        is_sufficient = coffeeMaker.is_resource_sufficient(drink)
        if is_sufficient:
            if moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)
