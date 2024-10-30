class Discount:
    """
    Class representing a Discount in the system.
    """
    def __init__(self, discount_type, percentage):
        # Discount attributes
        self._discount_type = discount_type
        self._percentage = percentage

    # Apply discount to a given amount
    def apply_discount(self, amount):
        discount_amount = amount * (self._percentage / 100)
        return amount - discount_amount

    # String representation for the Discount object
    def __str__(self):
        return f"Discount: {self._discount_type} at {self._percentage}%"
