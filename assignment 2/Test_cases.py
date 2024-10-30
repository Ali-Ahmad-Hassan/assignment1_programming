class Ebook:
    """
    Class representing an Ebook in the system.
    """
    def __init__(self, title, author, publication_date, genre, price):
        # Ebook attributes
        self._title = title
        self._author = author
        self._publication_date = publication_date
        self._genre = genre
        self._price = price

    # Getter and setter for title
    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    # Getter and setter for price
    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    # String representation for the Ebook object
    def __str__(self):
        return f"Ebook: {self._title} by {self._author}, Price: ${self._price}, Genre: {self._genre}"


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


# Test Case 1: Add/Modify/Remove a new e-book to the e-bookstore's catalog
print("Test Case 1: Add/Modify/Remove a new e-book to the catalog")
ebook1 = Ebook("Harry Potter", "J.K Rowling", "1950", "Fiction", 10.99)
print(ebook1)

# Modify e-book details
ebook1.set_title("Harry Potter - Revised Edition")
ebook1.set_price(12.99)
print("After modification:", ebook1)

# Test removing the e-book from a catalog (for this example, just delete the object)
del ebook1
print("Ebook removed from the catalog\n")

# Test Case 2: Add/Modify/Remove customer account
print("Test Case 2: Add/Modify/Remove customer account")
customer1 = Customer("Ali Ahmad", "ali@example.com")
print(customer1)

# Modify customer details
customer1.set_name("Ali Ahmad")
customer1.set_contact_info("ali.ahmad@example.com")
print("After modification:", customer1)

# Removing customer account (delete the object)
del customer1
print("Customer account removed\n")

# Test Case 3: The addition of e-books to the shopping cart
print("Test Case 3: The addition of e-books to the shopping cart")
customer2 = Customer("Ahmad  Ali", "ahmad@example.com")
cart = customer2.get_shopping_cart()

# Create e-books
ebook2 = Ebook("1984", "George Orwell", "1949", "Dystopian", 8.99)
ebook3 = Ebook("To Kill a Mockingbird", "Harper Lee", "1960", "Fiction", 7.99)

# Add e-books to shopping cart
cart.add_item(ebook2)
cart.add_item(ebook3)
print("Shopping Cart after adding e-books:", cart)

# Remove an e-book from the cart
cart.remove_item(ebook2)
print("Shopping Cart after removing an e-book:", cart, "\n")

# Test Case 4: Applying discounts for loyalty program members or bulk purchases
print("Test Case 4: Applying discounts for VIP loyalty program members")
vip_customer = VIPCustomer("Ali Ahmad", "ali@example.com", "Gold", 15.0)
print(vip_customer)

# Apply loyalty discount to a purchase amount
initial_amount = 50.0
discounted_amount = vip_customer.apply_loyalty_discount(initial_amount)
print(f"Initial Amount: ${initial_amount}, Discounted Amount for VIP: ${discounted_amount}\n")

# Test Case 5: The generation of an invoice showing relevant discounts and required payments
print("Test Case 5: Generation of invoice with discounts and payment")
order = Order()
order.add_ebook(ebook2)
order.add_ebook(ebook3)

# Generate an invoice for the order
invoice = Invoice(1, order.get_total_price(), tax_rate=0.08)
print("Invoice before discount:", invoice)

# Apply a discount to the order
bulk_discount = Discount("Bulk Purchase", 10)  # 10% discount
discounted_total = bulk_discount.apply_discount(order.get_total_price())
invoice_with_discount = Invoice(2, discounted_total, tax_rate=0.08)
print("Invoice after applying bulk discount:", invoice_with_discount)

# Process payment for the invoice
payment = Payment("Credit Card", invoice_with_discount._Invoice__total_with_tax)
print("Payment Processed:", payment.process_payment())
