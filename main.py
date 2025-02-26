from cart import Cart
from tablet import Tablet
from laptop import Laptop
from smartphone import Smartphone
from device import Device

devices = [
    Smartphone("iPhone 14", 999, 10, 24, 6.1, 20),
    Smartphone("Samsung Galaxy S22", 899, 15, 24, 6.2, 22),
    Laptop("MacBook Pro 16", 2499, 5, 36, 16, 3.2),
    Laptop("Dell XPS 13", 1299, 8, 24, 8, 2.8),
    Tablet("iPad Pro", 1099, 12, 24, "2388x1668", 468),
    Tablet("Samsung Galaxy Tab S8", 699, 10, 24, "2560x1600", 507)
]

cart = Cart()

# User Menu
def show_menu():
    while True:
        print("\n1. Show Devices\n2. Show Cart\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            for i, device in enumerate(devices, start=1):
                print(f"{i}. {device}")
            selection = int(input("Select a device to add to cart (0 to cancel): "))
            if selection > 0 and selection <= len(devices):
                quantity = int(input("Enter quantity: "))
                cart.add_device(devices[selection - 1], quantity)

        elif choice == "2":
            cart.print_items()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, please try again.")


# Run the application
show_menu()









