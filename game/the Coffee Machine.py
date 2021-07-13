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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficinet(order_ingredients):
    """This gives output is resources is sufficent for the prepeartion of the coffee"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coin():
    """Return the coin into $"""
    print("Please Enter the coin. ")
    total = int(input("how many quarters ?: ")) *0.25
    total += int(input("how many dimes ?: ")) *0.1
    total += int(input("how many nickles ?: ")) *0.05
    return total

    
def is_transaction_successful(money_received,drink_cost):
    """Return True when the payment is accepted or False if money is insufficent"""
    if money_received >= drink_cost :
        change=round(money_received - drink_cost,2)
        print(f"Here is change ${change} in change.")
        global profit
        profit += drink_cost
        return True 
    else:
        print("Sorry that's not enough money.Money refunded")
        return False 
       


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredinets from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ Enjoy ")





is_on = True
while is_on:
    choice = input("\n What would you like ? (espresso/latte/cappuccino): ")
    if choice =="off":
        is_on= False
    elif choice == "report":
       print(f"Water: {resources['water']} ml")
       print(f"Milk:  {resources['milk']} ml")
       print(f"Coffee: {resources['coffee']} ml") 
       print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficinet(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])
