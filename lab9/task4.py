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

# Example usage:
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("apple", 1.5)
    cart.add_item("banana", 2.0)
    cart.add_item("orange", 1.0)
    cart.add_item("milk", 3.5)
    print("Total cost:", cart.total_cost())
    cart.remove_item("apple")
    print("Total cost after removing apple:", cart.total_cost())