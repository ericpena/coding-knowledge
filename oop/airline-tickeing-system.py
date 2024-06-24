
# :: airline ticketing system design
# :: flight scheduling, booking, ticket pricing, and passenger management

# :: High Level Thoughts:
# :: Airline can contain several flights
# :: Flight can contain Passengers
# :: Ticket has a Passenger and Flight associated with it
# :: Booking acts as a transaction class -> generates a ticket
#----------------------------------
# :: Requirements
# :: Flights:
#       - departure
#       - arrival
#       - capacity
# :: Booking 
#       - book tickets to ensure not overbooking
#       - calculate ticket prices based on factors like seat and booking time
# :: Ticket
#       - has passenger information (perhaps the Passenger object)
#----------------------------------
# :: Other Thoughts
#       - perhaps there can be different kinds of tickets
#       - price should not be determined within the ticket class but perhaps the booking class

from abc import ABC, abstractmethod

class Passenger():

    def __init__(self, first_name, last_name, luggage=True):
        self.first_name = first_name
        self.last_name = last_name
        self.luggage = luggage


class Flight():

    def __init__(self, departure=None, arrival=None, capacity:int=None):
        # :: TODO Possibly convert departure and arrival to datetime types
        self.departure = departure
        self.arrival = arrival
        self.capacity = capacity
        self.passengers = []
        # :: TODO Consider whether passengers should be be included as a composition in this class
        
    # :: So that we can change departure and arrival times as needed later on
    def add_departure(self, departure):
        self.departure = departure
    
    def add_arrival(self, arrival):
        self.arrival = arrival

    def number_of_passengers(self):
        return len(self.passengers)

    def add_passenger(self, passenger: Passenger):
        if self.number_of_passengers() >= self.capacity:
            print('Unable to add passenger. Capacity Reached.')
            return
        else:
            self.passengers.append(passenger)

class Airline():

    def __init__(self, type='commercial'):
        self.flights = []
    
    def add_flight(self, flight: Flight):
        self.flights.append(flight)

    def remove_flight(self, flight):
        del self.flights[self.flights.index(flight)]

class Airport():

    def __init__(self):
        self.airlines = []
    
    def add_airline(self, airline : Airline):
        self.airlines.append(airline)
    
    def remove_airline(self, airline):
        del self.airlines[self.airlines.index(airline)]

class Ticket(ABC):

    def __init__(self, price, passenger: Passenger, flight: Flight):
        self._price = price
        self._passenger = passenger
        self._flight = flight

    @abstractmethod
    def set_price(self, price):
        pass

    @abstractmethod
    def get_price(self, price):
        pass

class FirstClassTicket(Ticket):

    def __init__(self, price, passenger: Passenger, flight: Flight):
        super().__init__(price, passenger, flight)

    def set_price(self, price):
        # :: If there aren't many seats left, make less expensive
        pass

    def get_price(self, price):
        pass

class BusinessTicket(Ticket):

    def __init__(self, price, passenger: Passenger, flight: Flight):
        super().__init__(price, passenger, flight)

    def set_price(self, price):
        # :: If there aren't many seats left, increase the price
        pass

    def get_price(self, price):
        pass

class CoachTicket(Ticket):

    def __init__(self, price, passenger: Passenger, flight: Flight):
        super().__init__(price, passenger, flight)

    def set_price(self, price):
        pass

    def get_price(self, price):
        pass

class Bookings():

    # :: design decision: need a way to captures all existing passenagers on this flight

    def __init__(self, airport):
        self.airport = airport
    
    def is_full(self):
        pass

def main():
    pass
    # :: Create Airline A
    # :: Create Airline B

    # :: Create Flight A
    # :: Create Flight B

    # :: Add flights to respective airlines

    # :: Add all the airlines to the airport


if __name__ == "__main__":
    main()