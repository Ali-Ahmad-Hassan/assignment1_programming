class Guest:
    """This class represents the hotel's guests"""

    # Guest's attributes
    def __init__(self, guest_id, guest_name, guest_email, g_Phone_number, reservation_list=None):
        self.__guest_id = guest_id  # Unique ID for the guest
        self.__guest_name = guest_name  # Guest's name
        self.__guest_email = guest_email  # Guest's email
        self.__g_Phone_number = g_Phone_number  # Guest's phone number
        self.__reservation_list = reservation_list if reservation_list else []  # Guest's reservation list (default is an empty list)

    # Set the guest's ID.
    def set_guest_id(self, guest_id):
        self.__guest_id = guest_id

    # Return the guest's ID.
    def get_guest_id(self):
        return self.__guest_id

    # Set the Guest Name
    def set_guest_name(self, guest_name):
        self.__guest_name = guest_name

    # Return the guest's name
    def get_guest_name(self):
        return self.__guest_name

    # Set the guest's email
    def set_guest_email(self, guest_email):
        self.__guest_email = guest_email

    # Return the guest's email
    def get_guest_email(self):
        return self.__guest_email

    # Set the Guest Phone Number
    def set_g_Phone_number(self, g_Phone_number):
        self.__g_Phone_number = g_Phone_number

    # Return the guest's phone number
    def get_g_Phone_number(self):
        return self.__g_Phone_number

    # Set the Reservation List
    def set_reservation_list(self, reservation_list):
        self.__reservation_list = reservation_list

    # Return the guest's reservation list
    def get_reservation_list(self):
        return self.__reservation_list
