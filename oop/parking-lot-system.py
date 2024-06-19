
from abc import ABC, abstractmethod
from collections import Counter

class Vehicle(ABC):

    def __init__(self, id, color):
        self.id = id
        self.color = color
    
    def get_color(self):
        return self.color
    
    @abstractmethod
    def get_wheels():
        pass

class Motorcycle(Vehicle):
    
    def __init__(self, id, color, style):
        super().__init__(id, color)
        self.style = style
    
    def get_wheels():
        pass

    @staticmethod
    def go_vroom():
        print('Vroom! Vroom!')

    # :: shows up when we use "print"
    def __str__(self):
        return f'{self.color} Motorcycle with style: {self.style}'
    
    # :: programmers details representation of the instantiated object
    def __repr__(self):
        return f'{self.color} Motorcycle with style: {self.style}'

class Car(Vehicle):
    pass

class Bus(Vehicle):
    pass

class ParkingSpot(ABC):
    
    def __init__(self, level, row, status):
        self.level = level
        self.row = row
        self.status = status

    @abstractmethod
    def occupy():
        pass
    @abstractmethod
    def empty():
        pass
    @abstractmethod
    def get_status():
        pass

class CompactSpot(ParkingSpot):
    
    def __init__(self, level, row, status):
        super().__init__(level, row, status)

    def occupy():
        pass
    
    def empty():
        pass
    
    def get_status():
        pass

class LargeSpot(ParkingSpot):

    def __init__(self, level, row, status):
        super().__init__(level, row, status)

    def occupy():
        pass
    
    def empty():
        pass
    
    def get_status():
        pass

class MotorCycleSpot(ParkingSpot):

    def __init__(self, level, row, status):
        super().__init__(level, row, status)    

    def occupy():
        pass
    
    def empty():
        pass
    
    def get_status():
        pass

class ParkingLot():

    def __init__(self, levels, rows):
        self.parkinglot = {i : [None]*rows for i in range(levels)}

    cs1 = CompactSpot(3, 5, 'empty')
    ms1 = MotorCycleSpot(2, 6, 'occupied')

    parking_spots = [cs1, ms1]

    mc = Motorcycle(1, 'blue', 'fast')
    print(mc)

    spot_counter = Counter([s.__class__.__name__ for s in parking_spots])
    print(spot_counter)

pl = ParkingLot(4, 5)
print(pl.parkinglot)
            