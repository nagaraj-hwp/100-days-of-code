# Creating a virtual coffee machine for new office
from art import broken, logo, coffee_art
# TODO: 1. Print report about the coffee machine
WATER_LEVEL = 700
MILK_LEVEL = 400
COFFEE_LEVEL = 200
# AMOUNT = 0

water_used = 0
milk_used = 0
coffee_used = 0
money = 0.00
print(logo)


def print_report():
    print(f"Water: {WATER_LEVEL - water_used}ml")
    print(f"Milk: {MILK_LEVEL - milk_used}ml")
    print(f"Coffee: {COFFEE_LEVEL - coffee_used}gm")
    print(f"Money: ${money}")


# TODO: 2. Check resources are sufficient
def is_resource_available(drink):
    water = WATER_LEVEL - water_used
    milk = MILK_LEVEL - milk_used
    coffee = COFFEE_LEVEL - coffee_used
    # print(water)
    # print(milk)
    # print(coffee)
    if drink == "expresso" and milk < 50 or coffee < 18:
        print(f"Can't have a espresso!, not enough resource, {broken}")
    elif drink == "latte" and water < 200 or milk < 150 or coffee < 24:
        print(f"Can't have a latte!, not enough resource,{broken}")
    elif drink == "cappuccino" and water < 250 or milk < 100 or coffee < 24:
        print(f"Can't have a cappuccino!, not enough resource, {broken}")
    else:
        return True
    return False


# TODO: 5. Make coffee as per requirement
def make_drink(drink):
    global water_used
    global milk_used
    global coffee_used
    global money
    if drink == "expresso":
        water_used += 50
        milk_used += 0
        coffee_used += 18
        money += 1.50
    elif drink == "latte":
        water_used += 200
        milk_used += 150
        coffee_used += 24
        money += 2.50
    elif drink == "cappuccino":
        water_used += 250
        milk_used += 100
        coffee_used += 24
        money += 3.00
    print(coffee_art)
    print("Enjoy your {drink}!!!")


# TODO: 4. Check the transaction successful
def check_transactions(drink, total_pennies):
    if drink == "expresso" and total_pennies < 150:
        print(f"Can't have a espresso!, not enough money, {broken}")
    elif drink == "latte" and total_pennies < 250:
        print(f"Can't have a latte!, not enough money,{broken}")
    elif drink == "cappuccino" and total_pennies < 300:
        print(f"Can't have a cappuccino!, not enough money, {broken}")
    else:
        make_drink(drink)


# TODO: 3. Process the coins inserted
def insert_coins():
    penny = int(input("How many pennies? "))
    nickel = int(input("How many nickels? "))
    dime = int(input("How many dimes? "))
    quarter = int(input("How many quarters? "))
    total_pennies = penny + nickel * 5 + dime * 10 + quarter * 25
    # print(total_pennies)
    return total_pennies


def start_machine():
    drink = input("What would you like to have?\n(Type 'E' for espresso)\n(Type 'L' for latte)\n(Type 'C' for "
                  "cappuccino)\n").lower()
    if drink == "expresso" or drink == "e":
        resource = is_resource_available("expresso")
        if resource:
            print("That will cost $1.50, Insert coins, extras cannot be returned")
            total_pennies = insert_coins()
            check_transactions("expresso", total_pennies)
    elif drink == "latte" or drink == "l":
        resource = is_resource_available("latte")
        if resource:
            print("That will cost $2.50, Insert coins, extras cannot be returned")
            total_pennies = insert_coins()
            check_transactions("latte", total_pennies)
    elif drink == "cappuccino" or drink == "c":
        resource = is_resource_available("cappuccino")
        if resource:
            print("That will cost $3.00, Insert coins, extras cannot be returned")
            total_pennies = insert_coins()
            check_transactions("cappuccino", total_pennies)
    elif drink == "report":
        print_report()
    else:
        print("Ohh!, the flavour that you liked is not available here", end="")
        print(broken)


need_coffee = True
while need_coffee:
    start_machine()
    need = input("Need one more coffee? 'Y' or 'N'\n").lower()
    if need != 'y':
        need_coffee = False

