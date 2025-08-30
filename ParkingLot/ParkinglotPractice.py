from enum import Enum


# The parking lot has multiple floors.
#
# Each floor has multiple parking spots.
#
# Vehicles can be of different types: bike, car, truck.
#
# The system should support:
#
# Park a vehicle
#
# Remove a vehicle
#
# Check available spots
#
# Each vehicle type can only park in compatible spots (e.g., a bike cannot occupy a truck spot).


from enum import Enum


class SpotType(Enum):
    Bike = 1
    Car = 2
    Truck = 3

class Vehicle:

    def __init__(self, make, model, year, spot_type):
        self.make = make
        self.model = model
        self.year = year
        self.spot_type = spot_type


class Car(Vehicle):

    def __init__(self, make, model, year, spot_type):
        super().__init__(make, model, year, spot_type)

class Bike(Vehicle):

    def __init__(self, make, model, year, spot_type):
        super().__init__(make, model, year, spot_type)

class Truck(Vehicle):

    def __init__(self, make, model, year, spot_type):
        super().__init__(make, model, year, spot_type)

class ParkingSpot:

    def __init__(self, spotType):
        self.spotType = spotType
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None

    def park(self, vehicle):
        if self.is_available() and vehicle.spot_type == self.spotType:
            self.vehicle = vehicle
            return True
        return False

    def unpark(self):
        if not self.is_available():
            self.vehicle = None
            return True
        return False

class Floor:

    def __init__(self, floor_number, spots_config):
        self.floor_number = floor_number
        self.spots = []
        for spot_type, count in spots_config.items():
            for _ in range(count):
                self.spots.append(ParkingSpot(spot_type))

    def park(self, vehicle):
        for spot in self.spots:
            if spot.park(vehicle):
                return True
        return False

    def unpark(self, vehicle):
        for spot in self.spots:
            if spot.vehicle == vehicle:
                return spot.unpark()
        return False

    def available_spots(self, spot_type=None):
        if spot_type:
            return sum(1 for spot in self.spots if spot.is_available() and spot.spotType == spot_type)
        return sum(1 for spot in self.spots if spot.is_available())

class ParkingLot:

    def __init__(self, num_floors, spots_config):
        self.floors = {}
        for i in range(num_floors):
            self.floors[i] = Floor(i, spots_config)

    def park(self, floor_number, vehicle):
        if floor_number not in self.floors:
            return False
        return self.floors[floor_number].park(vehicle)

    def unpark(self, floor_number, vehicle):
        if floor_number not in self.floors:
            return False
        return self.floors[floor_number].unpark(vehicle)

    def available_spots(self, floor_number, spot_type=None):
        if floor_number not in self.floors:
            return 0
        return self.floors[floor_number].available_spots(spot_type)

