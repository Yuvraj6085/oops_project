class Room:
    def __init__(self, number, room_type, price):
        self.number = number
        self.room_type = room_type
        self.price = price
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Booked"
        return f"Room {self.number} ({self.room_type}) - ₹{self.price} [{status}]"


class Booking:
    def __init__(self, customer_name, room):
        self.customer_name = customer_name
        self.room = room
        self.is_checked_in = False

    def check_in(self):
        if not self.is_checked_in:
            self.is_checked_in = True
            print(f"{self.customer_name} checked into Room {self.room.number}")
        else:
            print("Already checked in.")

    def check_out(self):
        if self.is_checked_in:
            self.is_checked_in = False
            self.room.is_available = True
            print(f" {self.customer_name} checked out from Room {self.room.number}")
        else:
            print("You are not checked in.")


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.bookings = []

    def add_room(self, room):
        self.rooms.append(room)

    def display_rooms(self):
        print(f"\n {self.name} - Room List")
        for room in self.rooms:
            print(room)

    def reserve_room(self, customer_name, room_number):
        for room in self.rooms:
            if room.number == room_number and room.is_available:
                room.is_available = False
                booking = Booking(customer_name, room)
                self.bookings.append(booking)
                print(f"Room {room.number} booked for {customer_name}")
                return booking
        print("Room not available.")

    def find_booking(self, customer_name):
        for booking in self.bookings:
            if booking.customer_name.lower() == customer_name.lower():
                return booking
        return None


hotel = Hotel("Grand Palace")
hotel.add_room(Room(101, "Single", 1500))
hotel.add_room(Room(102, "Double", 2500))
hotel.add_room(Room(103, "Suite", 5000))
hotel.display_rooms()
booking1 = hotel.reserve_room("Vinit Sharma", 102)
if booking1:
    booking1.check_in()
hotel.display_rooms()
if booking1:
    booking1.check_out()
hotel.display_rooms()
