# Create a Room object
room = Room(room_number=101, room_type="2 Queen Beds", price_per_night=89.85, is_available=False, bed_type="Queen")

# View room information
print(f"Room Number: {room.get_room_number()}")
print(f"Room Type: {room.get_room_type()}")
print(f"Price Per Night: ${room.get_price_per_night()}")
print(f"Room Availability: {room.get_is_available()}")
print(f"Bed Type: {room.get_bed_type()}")
