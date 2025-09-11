
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
#


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

class Bike(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year, SpotType.BIKE)

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year, SpotType.CAR)

class Truck(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year, SpotType.TRUCK)


class ParkingSpot:

    def __init__(self, spotType):
        self.spotType = spotType
        self.vehicles = None

    def is_available(self):
        return self.vehicles is None


    def park(self, vehicle):
        if self.is_available() and vehicle.spot_type == self.spot_type:
            self.vehicle = vehicle
            return True
        return False

    def unpark(self, vehicle):
        if self.vehicle:
            self.vehicle = None
            return True
        return False


class Floor:
    def __init__(self, number, spot_distribution):
        # spot_distribution = {SpotType.BIKE: 10, SpotType.CAR: 20, SpotType.TRUCK: 5}
        self.number = number
        self.spots = []
        for spot_type, count in spot_distribution.items():
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

    def available_spots(self):
        return sum(1 for spot in self.spots if spot.is_available)


class ParkingLot:
    def __init__(self, num_floors, spot_distribution):
        self.floors = {i: Floor(i, spot_distribution) for i in range(num_floors)}

    def park(self, floor, vehicle):
        if floor not in self.floors:
            return False
        return self.floors[floor].park(vehicle)

    def unpark(self, floor, vehicle):
        if floor not in self.floors:
            return False
        return self.floors[floor].unpark(vehicle)

    def check_available_spots(self, floor=None):
        if floor is not None:
            return self.floors[floor].available_spots()
        return {f: fl.available_spots() for f, fl in self.floors.items()}




