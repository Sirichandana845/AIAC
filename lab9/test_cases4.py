class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total_cost(self):
        return sum(self.items.values())

# Test cases
cart = ShoppingCart()

# Test add_item
cart.add_item("apple", 1.5)
cart.add_item("banana", 2.0)
cart.add_item("milk", 3.5)
print("Items after adding:", cart.items)
print("Total cost after adding:", cart.total_cost())

# Test remove_item
cart.remove_item("banana")
print("Items after removing banana:", cart.items)
print("Total cost after removing banana:", cart.total_cost())

# Test removing an item not in cart
cart.remove_item("bread")
print("Items after trying to remove bread (not in cart):", cart.items)
print("Total cost after trying to remove bread:", cart.total_cost())