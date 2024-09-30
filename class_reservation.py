class Reservation:
    """This class represents the reservations of the guests"""

    # Reservations attributes
    def __init__(self, reservation_id, check_in_date, check_out_date, room_number, total_price=0):
        self.__reservation_id = reservation_id  # Unique ID for the reservation
        self.__check_in_date = check_in_date  # Check-in date
        self.__check_out_date = check_out_date  # Check-out date
        self.__room_number = room_number  # Room number assigned to the reservation
        self.__total_price = total_price  # Total price for the reservation, default is 0

    # Sets Reservation ID
    def set_reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id

    # Returns Reservation ID
    def get_reservation_id(self):
        return self.__reservation_id

    # Sets Check-in Date
    def set_check_in_date(self, check_in_date):
        self.__check_in_date = check_in_date

    # Returns Check-in Date
    def get_check_in_date(self):
        return self.__check_in_date

    # Sets Check-out Date
    def set_check_out_date(self, check_out_date):
        self.__check_out_date = check_out_date

    # Returns Check-out Date
    def get_check_out_date(self):
        return self.__check_out_date

    # Sets Room Number
    def set_room_number(self, room_number):
        self.__room_number = room_number

    # Returns Room Number
    def get_room_number(self):
        return self.__room_number

    # Sets Total Price
    def set_total_price(self, total_price):
        self.__total_price = total_price

    # Returns Total Price
    def get_total_price(self):
        return self.__total_price

    # Calculate Total Price based on the number of the nights
    def calculate_total_price(self, price_per_night, nights):
        self.__total_price = price_per_night * nights


