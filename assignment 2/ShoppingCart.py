class ShoppingCart:
    """
    Class representing a Shopping Cart in the system.
    """
    def __init__(self):
        # Aggregation: ShoppingCart contains references to Ebook items
        self._items = []
        self._total = 0.0

    # Add an item (ebook) to the shopping cart
    def add_item(self, ebook):
        self._items.append(ebook)
        self._total += ebook.get_price()

    # Remove an item (ebook) from the shopping cart
    def remove_item(self, ebook):
        if ebook in self._items:
            self._items.remove(ebook)
            self._total -= ebook.get_price()

    # Get the total price of the cart
    def get_total(self):
        return self._total

    # String representation for the ShoppingCart object
    def __str__(self):
        return f"ShoppingCart with {len(self._items)} items, Total: ${self._total}"
