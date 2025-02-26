

class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            device.reduce_stock(amount)
        else:
            print("Not enough stock available!")

    def remove_device(self, device, amount):
        for i, (item, qty) in enumerate(self.items):
            if item == device:
                if amount >= qty:
                    self.total_price -= item.price * qty
                    self.items.pop(i)
                else:
                    self.items[i] = (item, qty - amount)
                    self.total_price -= item.price * amount
                break

    def print_items(self):
        for item, qty in self.items:
            print(f"{item.name} - Quantity: {qty}")
        print(f"Total Price: ${self.total_price}")

    def checkout(self):
        print("Processing your order...")
        self.print_items()
        self.items.clear()
        self.total_price = 0
        print("Order complete!")
