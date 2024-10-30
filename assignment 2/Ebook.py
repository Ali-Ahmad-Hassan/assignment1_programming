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
