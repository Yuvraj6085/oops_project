class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ₹{self.price}"


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)
        print(f"Added '{menu_item.name}' to cart.")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                print(f"Removed '{item.name}' from cart.")
                return
        print(" Item not found in cart.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("\n Your Cart:")
            total = 0
            for item in self.items:
                print(f"- {item.name} ₹{item.price}")
                total += item.price
            print(f"Total: ₹{total}")

    def checkout(self):
        if not self.items:
            print("Your cart is empty. Add items before checkout.")
            return
        total = sum(item.price for item in self.items)
        print("\nCheckout Successful!")
        print(f"Total amount to pay: ₹{total}")
        self.items.clear()


class Customer:
    def __init__(self, name):
        self.name = name
        self.order = Order()

    def place_order(self, menu):
        print("\nMenu:")
        for i, item in enumerate(menu, 1):
            print(f"{i}. {item}")
        choice = int(input("\nEnter item number to add to cart: "))
        if 1 <= choice <= len(menu):
            self.order.add_item(menu[choice - 1])
        else:
            print("Invalid choice.")

menu = [
    MenuItem("Burger", 120),
    MenuItem("Pizza", 250),
    MenuItem("Pasta", 150),
    MenuItem("Fries", 80),
    MenuItem("Cold Drink", 50)
]

customer = Customer("Vinit")

customer.place_order(menu)
customer.place_order(menu)
customer.order.view_cart()

customer.order.remove_item("Fries")
customer.order.view_cart()
customer.order.checkout()
