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

# 1. user prompt for drink
# 2. check if enough resources - return true or false
#. 3. if enough resources:
#   a) ask for money
#   b) make drink
#   c) deduct from resources.
#4. if not enough money, print not enough money . Give refund.
#5. If user types in report - return current resources and profit.
# 6. if user types in off - the program finishes.

def is_enough_resources(order_ingredients):
    #checks if current resources are enough to make a drink
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'Not enough {item}')
            return False
    return True


def order_cost(drink_order):
    amount_required = MENU[drink_order]["cost"]
    return amount_required

def money_difference(money_paid, money_required):
    money_diff = round(money_paid - money_required, 2)
    return money_diff

def is_enough_money(money_paid, coffee_cost):
    if money_paid <= coffee_cost:
        print(f"You did not pay enough money. Here is your refund £{money_paid}.")
        return False
    return True

def remaining_resources(drink_ingred, current_resources):
    for ingredient in drink_ingred:
        in_key, in_val = ingredient
        resources[in_key] = resources[in_key] - in_val
    return
# def report()


while True:

    drink = input("What would you like? (espresso/latte/cappuccino): ")
    drink_ingredients = MENU[drink]["ingredients"]
    print(f"{drink} ingredients are: {drink_ingredients}")
    if is_enough_resources(drink_ingredients):
        drink_cost = order_cost(drink)
        print(f"Your drink costs £{drink_cost}.")
        money = float(input("Please pay for your drink. £"))
        if is_enough_money(money, drink_cost):
            print(f"Here is your {drink}, enjoy!")
            change = money_difference(money, drink_cost)
            print(f"Here is your change of £{change}.")

        else:
            break

    else:
        break


