# Simple Cafe Menu Ordering System

# Menu stored as a dictionary
menu = {
    "Espresso": 100,
    "Cappuccino": 120,
    "Latte": 130,
    "Tea": 80,
    "Sandwich": 110
}

def display_menu():
    print("Welcome to Simple Cafe")
    print("Here is our menu:")
    for item, price in menu.items():
        print(f"- {item}: ₹{price}")
    print()

def take_order():
    item = input("Please enter the item you want to order: ").strip()
    if item in menu:
        print(f"The price of {item} is ₹{menu[item]}")
        confirm = input("Do you want to confirm the order? (yes/no): ").strip().lower()
        if confirm == "yes":
            print(f"Order confirmed for {item}. Thank you!")
        else:
            print("Order canceled.")
    else:
        print("Sorry, that item is not on the menu.")

# Main execution
display_menu()
take_order()
