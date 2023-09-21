# 1. user prompt for drink
# 2. check if enough resources 
# . 3. if enough resources:
#   a) ask for money, give change if due
#   b) make drink
#   c) deduct from resources.
# 4. if not enough money, print not enough money . Give refund.
# 5. if user enters "report" - return current resources and profit made so far.
# 6. if user enters "off" - exit the program.

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
    "water": 500,
    "milk": 300,
    "coffee": 200,
}


profit = 0


def exit_program():
    return exit()


def calculate_revenue(profit, beverage_choice):
    beverage_cost = MENU[beverage_choice]["cost"]
    profit += beverage_cost
    return profit


def statement_report(remaining_resources, revenue):
    print(f'Water: {remaining_resources["water"]}ml')
    print(f'Milk: {remaining_resources["milk"]}ml')
    print(f'Coffee: {remaining_resources["coffee"]}g')
    print(f"Money: £{revenue}")


def is_enough_resources(order_ingredients, resources):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'Sorry, there is not enough {item}.')
            return False
    return True


def order_cost(drink_order):
    amount_required = MENU[drink_order]["cost"]
    return amount_required


def money_difference(money_paid, money_required):
    money_diff = round(money_paid - money_required, 2)
    return money_diff


def is_enough_money(money_paid, coffee_cost):
    if money_paid < coffee_cost:
        print(f"You did not pay enough money. Here is your refund £{money_paid}.")
        return False
    return True


def deduct_from_resources(current_resources):
    drink_ingr = MENU[drink]["ingredients"]
    for key in drink_ingr:
        current_resources[key] = resources[key] - drink_ingr[key]
    return current_resources


def is_drink_in_menu_offer(beverage):
    while beverage not in MENU.keys():
        print("Please enter the correct beverage name.")
        return False
    return True


while True:

    drink = input("What would you like to drink? (espresso/latte/cappuccino): ")

    if drink == "off":
        exit_program()

    elif drink == "report":
        statement_report(resources, profit)

    elif is_drink_in_menu_offer(drink):
        drink_ingredients = MENU[drink]["ingredients"]
        print(f"{drink} ingredients are: {drink_ingredients}")
        print(f"Current resources are {resources}.")

        if is_enough_resources(drink_ingredients, resources):
            drink_cost = order_cost(drink)
            print(f"Your drink costs £{drink_cost}.")
            while True:
                money = input("Please pay for your drink. £")
                if money.isdigit():
                    money = float(money)
                    break
                elif isinstance(money, float):
                    break
                else:
                    print(f"Add some money please.")

            if is_enough_money(money, drink_cost):
                print(f"Here is your {drink}, enjoy!")
                change = money_difference(money, drink_cost)
                print(f"Here is your change of £{change}.")
                resources = deduct_from_resources(resources)
                print(f"The remaining resources are: {resources}.")
                profit = calculate_revenue(profit, drink)





    

          
        
