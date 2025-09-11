# LLD Question 2: Elevator (Lift) System
#
# Design a multi-elevator control system for a building.
#
# Requirements
#
# Building has N elevators and F floors.
#
# Users can make hall calls (Up/Down) and car calls (select floor inside elevator).
#
# Controller must assign requests to elevators (e.g., nearest-car / SCAN strategy).
#
# Elevator states: Idle, MovingUp, MovingDown, DoorOpen, Maintenance, Overloaded.
#
# Safety/ops:
#
# Door interlock (can’t move when door open),
#
# Overload blocks motion,
#
# Maintenance takes car out of service.
#
# Extensibility:
#
# Add new dispatching strategies without changing core.
#
# Add I/O adapters (buttons, sensors) without changing business logic.
#
# Your task (concise deliverable)
#
# List your key classes/interfaces, their responsibilities, and 2–3 core methods each. Aim to show SOLID:
#
# SRP (clean responsibilities)
#
# OCP (pluggable strategies, states)
#
# LSP (substitute strategies/states without surprises)
#
# ISP (thin interfaces for buttons/sensors)
#
# DIP (controller depends on abstractions)
#
# If you like, structure like this (example template):
#
# ElevatorCar — state, position, queue management
#
# requestStop(floor), step(), openDoor()
#
# ElevatorController — assigns hall calls
#
# handleHallCall(floor, dir), tick()
#
# DispatchStrategy (interface) — assign(elevators, call) -> carId
#
# ElevatorState (interface) — onTick(), onEnter(), onExit()
#
# Door, LoadSensor, PositionSensor (interfaces)
#
# Button abstractions: HallButton, CarButton
#
# EventBus (optional) for decoupled events


# left system, - N elevators and F floors.
# Users can make hall calls (Up/Down) and car calls (select floor inside elevator).



from abc import ABC, abstractmethod
from typing import List, Optional


from enum import Enum

class ElevatorState(Enum):
    IDLE = 1
    MOVING_UP = 2
    MOVING_DOWN = 3
    DOOR_OPEN = 4
    MAINTENANCE = 5
    OVERLOADED = 6


class Direction(Enum):
    UP = 1
    DOWN = 2


class HallCall:
    def __init__(self, floor: int, direction: Direction):
        self.floor = floor
        self.direction = direction


class CarCall:
    def __init__(self, floor: int, elevator_id: int):
        self.floor = floor
        self.elevator_id = elevator_id


class ElevatorCar:
    def __init__(self, elevator_id: int, capacity: int, sensors, door):
        self.elevator_id = elevator_id
        self.capacity = capacity

        # State
        self.state = ElevatorState.IDLE
        self.current_floor = 0
        self.direction = None  # Direction.UP / DOWN
        self.requests = []  # could be sorted list, heaps, etc.

        # Safety
        self.door = door
        self.sensors = sensors  # dict with load, position, etc.


    def requestStop(self, floor: int):
        """Add a car call (inside elevator)"""
        if floor not in self.requests:
            self.requests.append(floor)
            self.requests.sort()  # naive; replace with heaps in real impl

        if self.requests:
            target = self.requests[0]
            if self.current_floor < target:
                self.state = ElevatorState.MOVING_UP
                self.current_floor += 1
            elif self.current_floor > target:
                self.state = ElevatorState.MOVING_DOWN
                self.current_floor -= 1
            else:
                # Arrived at target
                self.openDoor()
                self.requests.pop(0)
        else:
            self.state = ElevatorState.IDLE

    def handleCarCall(self, car_call: CarCall):
        self.requestStop(car_call.floor)

    def openDoor(self):
        if not self.sensors["load"].isOverloaded():
            self.state = ElevatorState.DOOR_OPEN
            self.door.unlock()

    def closeDoor(self):
        self.door.lock()
        if not self.requests:
            self.state = ElevatorState.IDLE


class ElevatorController:
    def __init__(self, num_floors: int, elevators: list, strategy):
        self.num_floors = num_floors
        self.elevators = elevators  # List[ElevatorCar]
        self.strategy = strategy  # DispatchStrategy
        self.pending_hall_calls = []

    def handleHallCall(self, hall_call: HallCall):
        elevator = self.strategy.assign(self.elevators, hall_call)
        if elevator:
            elevator.requestStop(hall_call.floor)
        else:
            # if no elevator available, keep pending
            self.pending_hall_calls.append(hall_call)

    def tick(self):
        """Simulate one time step for the whole system"""
        # Assign pending hall calls again
        still_pending = []
        for call in self.pending_hall_calls:
            elevator = self.strategy.assign(self.elevators, call)
            if elevator:
                elevator.requestStop(call.floor)
            else:
                still_pending.append(call)
        self.pending_hall_calls = still_pending

        # Move each elevator one step
        for elevator in self.elevators:
            elevator.step()

    def setDispatchStrategy(self, strategy):
        """Plug in a new strategy at runtime"""
        self.strategy = strategy


class DispatchStrategy(ABC):
    @abstractmethod
    def assign(self, elevators: List[ElevatorCar], hall_call: HallCall) -> Optional[ElevatorCar]:
        pass


class NearestCarStrategy(DispatchStrategy):
    def assign(self, elevators, hall_call):
        best = None
        best_distance = float('inf')
        for e in elevators:
            if e.state not in [ElevatorState.MAINTENANCE, ElevatorState.OVERLOADED]:
                dist = abs(e.current_floor - hall_call.floor)
                if dist < best_distance:
                    best_distance = dist
                    best = e
        return best