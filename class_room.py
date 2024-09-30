class Room:
    """This class represents the room of the Hotel"""

    # Room's Attributes
    def __init__(self, room_number, room_type, price_per_night, is_available, bed_type):
        self.room_number = room_number  # Unique room number
        self.room_type = room_type  # Type of room (e.g., King, Queen)
        self.price_per_night = price_per_night  # Price per night
        self.is_available = is_available  # Room availability status
        self.bed_type = bed_type  # Type of bed in the room

    # Sets the Room Number
    def set_room_number(self, room_number):
        self.room_number = room_number

    # Returns the Room Number
    def get_room_number(self):
        return self.room_number

    # Sets the Room Type
    def set_room_type(self, room_type):
        self.room_type = room_type

    # Returns the Room Type
    def get_room_type(self):
        return self.room_type

    # Sets the Price Per Night
    def set_price_per_night(self, price_per_night):
        self.price_per_night = price_per_night

    # Returns the Price Per Night
    def get_price_per_night(self):
        return self.price_per_night

    # Sets the availability of the room
    def set_is_available(self, is_available):
        self.is_available = is_available

    # Returns the availability of the room
    def get_is_available(self):
        return self.is_available

    # Sets the Bed Type in the room
    def set_bed_type(self, bed_type):
        self.bed_type = bed_type

    # Returns the Bed Type in the room
    def get_bed_type(self):
        return self.bed_type


