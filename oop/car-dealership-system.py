"""
Vehicle Inventory System
"""
# :: parent class
class Vehicle:

    MANUFACTURED=0

    def __init__(self, vin: str, make: str, model: str, year: int, mileage: int, price: float):
        self._vin = vin
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price
        Vehicle.MANUFACTURED += 1
    
    def __str__(self):
        return f'vin: {self._vin}\nmake: {self.make}\nmodel: {self.model}\nyear: {self.year}\nmileage: {self.mileage}\nprice: {self.price}\n'

    def get_info(self) -> None:
        return f'vin: {self._vin}\nmake: {self.make}\nmodel: {self.model}\nyear: {self.year}\nmileage: {self.mileage}\nprice: {self.price}\n'
    
    def get_vin(self):
        return self._vin
    
    @staticmethod
    def go_vroom():
        print('VROOM! VROOM!')

    @classmethod
    def manufactured(cls):
        print(f'MANUFACTURED: {cls.MANUFACTURED}')

class Car(Vehicle):

    def __init__(self, vin, make, model, year, mileage, price, doors=4, convertible=False):

        super().__init__(vin, make, model, year, mileage, price)
        self.doors = doors
        self.convertible = convertible

    def __str__(self):
        return f'vin: {self._vin}\nmake: {self.make}\nmodel: {self.model}\nyear: {self.year}\nmileage: {self.mileage}\nprice: {self.price}\ndoors: {self.doors}\nconvertible: {self.convertible}'

    def get_info(self) -> None:
        return f'vin: {self._vin}\nmake: {self.make}\nmodel: {self.model}\nyear: {self.year}\nmileage: {self.mileage}\nprice: {self.price}\ndoors: {self.doors}\nconvertible: {self.convertible}'

class Truck(Vehicle):

    def __init__(self, vin, make, model, year, mileage, price, bed_length=6, four_wheel_drive=True):
        super().__init__(vin, make, model, year, mileage, price)
        self.bed_length = bed_length
        self.four_wheel_drive = four_wheel_drive

    # :: could go back and redefine __str__ and __repr__ and can override the get_info method to be specific for class
    
class Motorcycle(Vehicle):

    def __init__(self, vin, make, model, year, mileage, price, engine_cc):
        super().__init__(vin, make, model, year, mileage, price)
        self.engine_cc = engine_cc

    # :: could go back and redefine __str__ and __repr__ and can override the get_info method to be specific for class

class Inventory():

    # :: consider dataframe or dictionary (hashmap)
    # ::    add: new_row = pd.DataFrame({'vin':[vin], 'vehicle':[object]})
    # ::         df = pd.concat([df, new_row], ignore_index)
    # ::    remove: df.drop(index=df[df['vin'] == vin].index)
    # :: map: vin --> object
    # ::    add: dict[vin] = object
    # ::    remove: del dict[vin] or dict.pop(key, "key not found")
    def __init__(self):
        # :: could improve code implementing getting and setter methods
        # :: for the time being we'll make this attribute private
        self._inventory = {}
    
    def add_vehicle(self, vehicle):

        if vehicle.get_vin() not in self._inventory:
            self._inventory[vehicle.get_vin()] = vehicle
        else:
            print('Vehicle is already recorded.')

    def remove_vehicle(self, vehicle):

        self._inventory.pop(vehicle.get_vin(), 'Unable to remove. Vehicle not in inventory.')

    def get_vehicle_info(self, vin):

        print(self._inventory[vin].get_info())

    def list_vehicles(self, vehicle_type=None):

        for vin, veh in self._inventory.items():
            if (str(vehicle_type) in str(type(veh))) or (vehicle_type == None):
                print('-----------------------')
                print(vin)
                print(veh.get_info())

        # :: The better way to do this:
    def list_vehicles_better(self, vehicle_type=None):
        if vehicle_type:
            return [v.get_info() for v in self._inventory.values() if v.__class__.__name__ == vehicle_type]
        return [v.get_info() for v in self.vehicles]


def main():
    # :: make a bunch of vehicles
    car1 = Car('1HGCM82633A004352', 'Honda', 'Accord', 2020, 15000, 20000, 4, False)
    truck1 = Truck('1FTFW1E57JFA30456', 'Ford', 'F-150', 2018, 30000, 25000, 6, True)
    motorcycle1 = Motorcycle('2C3CDXBG3DH511614', 'Harley-Davidson', 'Street 750', 2019, 5000, 7500, 750)
    
    # :: add them to inventory
    inventory = Inventory()
    inventory.add_vehicle(car1)
    inventory.add_vehicle(truck1)
    inventory.add_vehicle(motorcycle1)
    
    # :: list vehicles of a certain type
    inventory.list_vehicles()
    # print(type(car1))
    inventory.list_vehicles('Car')

    print(inventory.list_vehicles_better('Car'))
    print(inventory.list_vehicles_better('Truck'))

    # :: Don't need an instantiation for @staticmethod or @classmethods
    Vehicle.go_vroom()

    # :: prints the number of vehicles created regardless of what kind of vehicle (look at Vehicle.__init___)
    Vehicle.manufactured()

    # :: remove vehicles

if __name__ == '__main__':
    main()