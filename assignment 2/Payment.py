class Payment:
    """
    Class representing a Payment for an Order.
    """
    def __init__(self, payment_method, amount_paid):
        # Payment attributes
        self._payment_method = payment_method
        self._amount_paid = amount_paid

    # Process the payment
    def process_payment(self):
        return f"Payment of ${self._amount_paid} processed via {self._payment_method}"

    # String representation for the Payment object
    def __str__(self):
        return f"Payment of ${self._amount_paid} via {self._payment_method}"
