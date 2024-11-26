
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
    "money": 0,
}


# TODO 1: Print Report
def report():
    for resource in resources:
        if resource == "water" or resource == "milk":
            print(f"{resource.capitalize()}: {resources[resource]}ml")
        elif resource == "coffee":
            print(f"{resource.capitalize()}: {resources[resource]}g")
        elif resource == "money":
            print(f"{resource.capitalize()}: ${resources[resource]:.2f}")

# TODO 2: Check if Resources are Sufficient
def resources_sufficient(chosen_coffee):

    ingredients = MENU[chosen_coffee]["ingredients"]

    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False

    return  True

# TODO 3: Process the Coins
def process_coins(chosen_coffee):
    cost = MENU[chosen_coffee]["cost"]
    print("Please insert coins.")

    total_amount = (
            int(input("How many quarters?:")) * 0.25 +
            int(input("How many dimes?:")) * 0.10 +
            int(input("How many nickles?:")) * 0.05 +
            int(input("How many pennies?:")) * 0.01
    )

    if total_amount < cost:
        print("Sorry, that's not enough money. Money Refunded")
        return False
    return total_amount

def transaction_successful(chosen_coffee, given_money):

    ingredients = MENU[chosen_coffee]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    resources["money"] += MENU[chosen_coffee]["cost"]
    change = given_money - MENU[chosen_coffee]["cost"]
    if change > 0:
        print(f"Here is ${change} in change.")

    print(f"Here is your {chosen_coffee} ☕️. Enjoy!")




def coffee_machine():
    machine_on = True
    while machine_on:
        order_place = input("What would you like? (espresso/ latte/ cappuccino):").lower()
        if order_place == "off":
            machine_on = False
            print("Turning off the machine. Goodbye!")
            break
        elif order_place == "report":
            report()
        elif order_place in MENU:
            if resources_sufficient(order_place):
                payment = process_coins(order_place)
                if payment:
                    transaction_successful(order_place, given_money=payment)

        else:
            print("Invalid Input")


coffee_machine()

