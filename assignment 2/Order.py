
class Order:
    """
    Class representing an Order in the system.
    """
    def __init__(self):
        # Composition: Order contains Ebook items specific to the order
        self._order_items = []
        self._total_price = 0.0
        # Composition: Each Order has one Payment instance associated with it
        self._payment = None

    # Add an ebook to the order
    def add_ebook(self, ebook):
        self._order_items.append(ebook)
        self._total_price += ebook.get_price()

    # Remove an ebook from the order
    def remove_ebook(self, ebook):
        if ebook in self._order_items:
            self._order_items.remove(ebook)
            self._total_price -= ebook.get_price()

    # Set payment for the order
    def set_payment(self, payment):
        self._payment = payment  # Composition: Payment is tied to the lifecycle of the order

    # Get the total price of the order
    def get_total_price(self):
        return self._total_price

    # Finalize the order
    def finalize_order(self):
        return f"Order finalized with total price: ${self._total_price}"

    # String representation for the Order object
    def __str__(self):
        return f"Order with {len(self._order_items)} items, Total: ${self._total_price}"
