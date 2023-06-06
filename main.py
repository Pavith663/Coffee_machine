MENU = {"espresso": {"ingredients": {"water": 50, "milk": 0, "coffee": 18, }, "cost": 1.5, },
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
}


def inventory():
    for item in resources:
        if resources[item] >= MENU[choice]['ingredients'][item]:
            resources[item] -= MENU[choice]['ingredients'][item]
        else:
            print("Insufficient resources")

    print("\nResources left\n ")
    for key, value in resources.items():
        print("{}: {}".format(key, value))




def payment():
    print(f"Cost: ${MENU[choice]['cost']}")
    print("\nPlease insert coins\n ")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))

    paid = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01

    if paid < MENU[choice]['cost']:
        print("Insufficient amount")
        print("\nResources left\n ")
        for key, value in resources.items():
            print("{}: {}".format(key, value))
        payment()
    elif paid == MENU[choice]['cost']:
        print("Thank you")
    else:
        change = paid - MENU[choice]['cost']
        print(f"${round(change,2)} is your change")


end = False
while not end:
    choice = input("Do you want an espresso, latte or cappuccino? Type no if you don't want any of the above. ").lower()
    if choice == 'no':
        end = True
    elif choice not in MENU.keys():
        print("wrong item")
        exit()
    else:
        payment()
        inventory()
