# Create a Reservation object
reservation = Reservation(reservation_id=52350867, check_in_date="Sat, Aug 22, 2010", check_out_date="Tue, Aug 24, 2010", room_number=101)

# Calculate total price for the reservation (2 nights)
reservation.calculate_total_price(price_per_night=89.85, nights=2)

# View reservation information
print(f"Reservation ID: {reservation.get_reservation_id()}")
print(f"Check-in Date: {reservation.get_check_in_date()}")
print(f"Check-out Date: {reservation.get_check_out_date()}")
print(f"Room Number: {reservation.get_room_number()}")
print(f"Total Price: ${reservation.get_total_price()}")
