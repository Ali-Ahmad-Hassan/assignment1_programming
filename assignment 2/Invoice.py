class Invoice:
    """
    Class representing an Invoice for an Order.
    """
    def __init__(self, invoice_number, order_total, tax_rate=0.08):
        # Private attributes for the invoice
        self.__invoice_number = invoice_number
        self.__total_with_tax = order_total + (order_total * tax_rate)
        # Aggregation: Invoice can contain multiple discounts
        self._discounts = []

    # Add a discount to the invoice
    def add_discount(self, discount):
        self._discounts.append(discount)

    # Get invoice details
    def get_invoice_details(self):
        return f"Invoice No: {self.__invoice_number}, Total with tax: ${self.__total_with_tax}"

    # String representation for the Invoice object
    def __str__(self):
        return self.get_invoice_details()
