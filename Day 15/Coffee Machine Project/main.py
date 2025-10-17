MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}

# TODO 1: Create report function to display the available resources
def report():
    print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${resources['money']}")

# TODO 2: Check if resource is sufficient
def is_resources_sufficient(drink):
    enough = []

    if drink == "espresso":
        enough.append(compare(drink,'water'))
        enough.append(compare(drink,'coffee'))
    elif drink == "latte":
        enough.append(compare(drink,'water'))
        enough.append(compare(drink,'milk'))
        enough.append(compare(drink,'coffee'))
    else:
        enough.append(compare(drink,'water'))
        enough.append(compare(drink,'milk'))
        enough.append(compare(drink,'coffee'))

    if False in enough:
        return False
    else:
        return True

def compare(drink, ingredient):
    if resources[ingredient] < MENU[drink]['ingredients'][ingredient]:
        print("Sorry there is not enough " + ingredient)
        return False
    else:
        return True

# TODO 3: Process coins
def insert_coins(choice):
    print("Please insert coins.")
    quarters = int(input("how many quarters?"))
    dimes = int(input("how many dimes?"))
    nickles = int(input("how many nickles?"))
    pennies = int(input("how many pennies?"))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    print(MENU[choice]['cost'])
    if total < MENU[choice]['cost']:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
        resources['money'] += MENU[choice]['cost']
# TODO 4: Complete the transaction
        if total - MENU[choice]['cost'] > 0:
            print("Here is " + str(round(total - MENU[choice]['cost'], 2)) + " dollars in change")
        return True

# TODO 5: Make coffee
def make_coffee(choice):
    for i in MENU[choice]['ingredients']:
        resources[i] -=  MENU[choice]['ingredients'][i]
    print("Here is your espresso ☕. Enjoy!")

TurnOn = True
while TurnOn:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        TurnOn = False
    elif choice == 'report':
        report()
    else:
        is_sufficient = is_resources_sufficient(choice)
        if is_sufficient:
            if(insert_coins(choice)):
                make_coffee(choice)