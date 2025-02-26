# Electronic Device Shopping Cart

## Description
A simple shopping cart system for electronic devices using Object-Oriented Programming (OOP) concepts in Python.

## Features
- Add/remove devices to/from cart
- Apply discounts
- Simulate checkout process

## Installation
Clone the repository and run the script:
```sh
git clone https://github.com/your-username/Electronic-Device-Cart.git
cd Electronic-Device-Cart
python main.py```

## Sample Input/Output
```1. Show Devices
2. Show Cart
3. Exit
Enter your choice: 1```


# Displaying Devices (Input: 1)


1. iPhone 14 - $999, Stock: 10, Warranty: 24 months, Screen: 6.1 inches, Battery: 20 hours
2. Samsung Galaxy S22 - $899, Stock: 15, Warranty: 24 months, Screen: 6.2 inches, Battery: 22 hours
3. MacBook Pro 16 - $2499, Stock: 5, Warranty: 36 months, RAM: 16GB, CPU: 3.2GHz
4. Dell XPS 13 - $1299, Stock: 8, Warranty: 24 months, RAM: 8GB, CPU: 2.8GHz
5. iPad Pro - $1099, Stock: 12, Warranty: 24 months, Resolution: 2388x1668, Weight: 468g
6. Samsung Galaxy Tab S8 - $699, Stock: 10, Warranty: 24 months, Resolution: 2560x1600, Weight: 507g
Select a device to add to cart (0 to cancel): 2
Enter quantity: 2


#Output after adding device:
Added 2 Samsung Galaxy S22 to the cart.

#Viewing Cart (Input: 2)
1. Samsung Galaxy S22 - Quantity: 2
Total Price: $1798

#Adding More Items
Enter your choice: 1
Select a device to add to cart (0 to cancel): 3
Enter quantity: 1

#Output:
Added 1 MacBook Pro 16 to the cart.

Viewing Updated Cart
Enter your choice: 2

#Output:
1. Samsung Galaxy S22 - Quantity: 2
2. MacBook Pro 16 - Quantity: 1
Total Price: $4297

# Removing an Item

Enter your choice: 2
Remove an item from cart? (yes/no): yes
Enter device number to remove: 1
Enter quantity to remove: 1

#Output:
Updated Cart:
1. Samsung Galaxy S22 - Quantity: 1
2. MacBook Pro 16 - Quantity: 1
Total Price: $3398

#Checkout Process
Enter your choice: 2
Checkout? (yes/no): yes

#Output:
Processing your order...
Samsung Galaxy S22 - Quantity: 1
MacBook Pro 16 - Quantity: 1
Total Price: $3398
Order complete!
📌 Exiting the Program (Input: 3)
Exiting program...

