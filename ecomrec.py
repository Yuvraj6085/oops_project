import json
import os
from datetime import datetime

class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def to_dict(self):
        return {"pid": self.pid, "name": self.name, "price": self.price}

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})
        print(f" Added {quantity} x {product.name} to cart.")

    def remove_product(self, pid):
        for item in self.items:
            if item["product"].pid == pid:
                self.items.remove(item)
                print(f" Removed {item['product'].name} from cart.")
                return
        print("Product not found in cart.")

    def view_cart(self):
        if not self.items:
            print(" Cart is empty.")
            return
        total = 0
        print("\nCart Items:")
        for item in self.items:
            p = item["product"]
            qty = item["quantity"]
            print(f"{p.name} x{qty} - ₹{p.price * qty}")
            total += p.price * qty
        print(f"Total: ₹{total}")

    def get_total(self):
        return sum(item["product"].price * item["quantity"] for item in self.items)

class Order:
    def __init__(self, customer_name, cart, payment_method):
        self.customer_name = customer_name
        self.cart = cart
        self.payment_method = payment_method
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.total_amount = cart.get_total()

    def to_dict(self):
        return {
            "customer_name": self.customer_name,
            "payment_method": self.payment_method,
            "date": self.date,
            "total_amount": self.total_amount,
            "items": [
                {"pid": i["product"].pid, "name": i["product"].name, "quantity": i["quantity"], "price": i["product"].price}
                for i in self.cart.items
            ]
        }

class ECommerceSystem:
    def __init__(self, order_file="orders.json"):
        self.products = []
        self.order_file = order_file
        if not os.path.exists(order_file):
            with open(order_file, "w") as f:
                json.dump([], f)

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print("\nProduct List:")
        for p in self.products:
            print(f"{p.pid}. {p.name} - ₹{p.price}")

    def save_order(self, order):
        with open(self.order_file, "r") as f:
            orders = json.load(f)
        orders.append(order.to_dict())
        with open(self.order_file, "w") as f:
            json.dump(orders, f, indent=2)
        print("Order saved successfully.")

system = ECommerceSystem()
system.add_product(Product(1, "Laptop", 60000))
system.add_product(Product(2, "Smartphone", 25000))
system.add_product(Product(3, "Headphones", 2000))

cart = Cart()
system.display_products()
cart.add_product(system.products[0], 1)
cart.add_product(system.products[2], 2)
cart.view_cart()

payment_method = input("\nEnter payment method (Cash, Card, UPI): ")
order = Order("Vinit Sharma", cart, payment_method)
system.save_order(order)
