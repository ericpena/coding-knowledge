from datetime import datetime
from abc import ABC, abstractmethod

class Airline:
    def __init__(self, name):
        self.name = name
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def get_flights(self):
        return self.flights

class Flight:
    def __init__(self, flight_number, departure, arrival, capacity):
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival
        self.capacity = capacity
        self.bookings = []

    def book_ticket(self, ticket):
        if len(self.bookings) < self.capacity:
            self.bookings.append(ticket)
            return True
        return False

    def get_bookings(self):
        return self.bookings

class Ticket(ABC):
    def __init__(self, passenger, flight):
        self.passenger = passenger
        self.flight = flight
        self.price = self.calculate_price()

    @abstractmethod
    def calculate_price(self):
        pass

class EconomyTicket(Ticket):
    def calculate_price(self):
        return 100  # base price for economy

class BusinessTicket(Ticket):
    def calculate_price(self):
        return 200  # base price for business

class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number

class Booking:
    def __init__(self, passenger, flight, ticket_type):
        self.passenger = passenger
        self.flight = flight
        self.ticket_type = ticket_type
        self.ticket = self.create_ticket()

    def create_ticket(self):
        if self.ticket_type == "economy":
            return EconomyTicket(self.passenger, self.flight)
        elif self.ticket_type == "business":
            return BusinessTicket(self.passenger, self.flight)

# Example usage
airline = Airline("Example Air")
flight = Flight("EX123", datetime(2024, 7, 1, 14, 0), datetime(2024, 7, 1, 18, 0), 100)
airline.add_flight(flight)

passenger = Passenger("John Doe", "P12345678")
booking = Booking(passenger, flight, "economy")

if flight.book_ticket(booking.ticket):
    print(f"Booked {booking.ticket_type} ticket for {passenger.name} on flight {flight.flight_number}. Price: ${booking.ticket.price}")
else:
    print("Booking failed. Flight is full.")
