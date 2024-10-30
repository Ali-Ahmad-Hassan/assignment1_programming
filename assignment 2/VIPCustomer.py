class VIPCustomer(Customer):
    """
    Class representing a VIP Customer, inheriting from Customer.
    """

    def __init__(self, name, contact_info, membership_level, extra_discount):
        # Initialize the base class (Customer) attributes
        super().__init__(name, contact_info)

        # VIPCustomer-specific attributes
        self._membership_level = membership_level  # The membership level of the VIP customer (e.g., 'Gold')
        self._extra_discount = extra_discount  # Additional discount percentage for VIP customers

    # Getter and setter for membership level
    def get_membership_level(self):
        return self._membership_level

    def set_membership_level(self, membership_level):
        self._membership_level = membership_level

    # Getter and setter for extra discount
    def get_extra_discount(self):
        return self._extra_discount

    def set_extra_discount(self, extra_discount):
        self._extra_discount = extra_discount

    # Method to apply an additional loyalty discount
    def apply_loyalty_discount(self, amount):
        # Calculates the amount after applying the extra discount
        discount_amount = amount * (self._extra_discount / 100)
        return amount - discount_amount

    # String representation for VIPCustomer
    def __str__(self):
        return (f"VIPCustomer: {self._name}, Contact: {self._contact_info}, "
                f"Membership Level: {self._membership_level}, Extra Discount: {self._extra_discount}%, "
                f"Cart Total: ${self._shopping_cart.get_total()}")
