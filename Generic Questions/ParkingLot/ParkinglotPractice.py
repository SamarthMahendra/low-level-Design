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
    BIKE = 1
    CAR = 2
    TRUCK = 3


class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Bike(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.spot_type = SpotType.BIKE

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.spot_type = SpotType.CAR

class Truck(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.spot_type = SpotType.TRUCK

class ParkingSpot:

    def __init__(self, spot_type):
        self.spot_type = spot_type
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None

    def park(self, vehicle):
        if self.is_available() and vehicle.spot_type == self.spot_type:
            self.vehicle = vehicle
            return True
        return False

    def unpark(self):
        if not self.is_available():
            vehicle = self.vehicle
            self.vehicle = None
            return vehicle
        return None


class Floor:

    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.spots = {
            SpotType.BIKE: [ParkingSpot(SpotType.BIKE) for _ in range(10)],
            SpotType.CAR: [ParkingSpot(SpotType.CAR) for _ in range(20)],
            SpotType.TRUCK: [ParkingSpot(SpotType.TRUCK) for _ in range(5)],
        }

    def park(self, vehicle):
        if vehicle.spot_type not in self.spots:
            return False
        for spot in self.spots[vehicle.spot_type]:
            if spot.park(vehicle):
                return True
        return False

    def unpark(self, vehicle):
        if vehicle.spot_type not in self.spots:
            return False
        for spot in self.spots[vehicle.spot_type]:
            if spot.vehicle == vehicle:
                spot.unpark()
                return True
        return False

    def available_spots(self, spot_type):
        if spot_type not in self.spots:
            return 0
        return sum(1 for spot in self.spots[spot_type] if spot.is_available())

class ParkingLot(ParkingSpot):

    def __init__(self, floors):
        self.floors = {}
        for i in range(floors):
            self.floors[i] = Floor(i)

    def park(self, floor, vehicle):
        if floor not in self.floors:
            return False
        return self.floors[floor].park(vehicle)

    def unpark(self, floor, vehicle):
        if floor not in self.floors:
            return False
        return self.floors[floor].unpark(vehicle)


