class Customer:
    """
    Class representing a Customer in the system.
    """
    def __init__(self, name, contact_info):
        # Customer attributes
        self._name = name
        self._contact_info = contact_info
        # Composition: Customer "owns" ShoppingCart, created upon Customer creation
        self._shopping_cart = ShoppingCart()

    # Getter and setter for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and setter for contact_info
    def get_contact_info(self):
        return self._contact_info

    def set_contact_info(self, contact_info):
        self._contact_info = contact_info

    # Getter for shopping cart
    def get_shopping_cart(self):
        return self._shopping_cart

    # String representation for the Customer object
    def __str__(self):
        return f"Customer: {self._name}, Contact: {self._contact_info}, Cart Total: ${self._shopping_cart.get_total()}"
