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
# Parking lot - class
# Multiple floors - class
# floor - multiplle spots
# vehicles - bike car, truck
#

class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Bike(Vehicle):

    def __int__(self, make, model, year):
        super().__int__(make, model, year)

class Truck(Vehicle):
    def __int__(self, make, model, year):
        super().__int__(make, model, year)

class Car(Vehicle):
    def __int__(self, make, model, year):
        super().__int__(make, model, year)


class ParkingLot:

    def __init__(self, floor):
        self.floors = {}
        for i in range(floor):
            self.floors[i] = Floor(i)

    def park(self, floor, vehicle):
        if floor not in self.floors:
            return False
        else:
            return self.floors[floor].park(vehicle)

    def unpark(self, floor, vehicle):
        if floor not in self.floors:
            return False
        else:
            return self.floors[floor].unpark(vehicle)




class Floor:

    def __init__(self, number):
        self.number = number
        self.capacity = 0
        self.vehicles = []

    def park(self):
        self.capacity += 1
        self.vehicles.append(Vehicle(self.number, self.number, self.number))

    def unpark(self, vehicle):
        self.capacity -= 1
        self.vehicles.remove(vehicle)








