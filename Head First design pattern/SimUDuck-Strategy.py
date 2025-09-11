from abc import ABC, abstractmethod

# --- Behavior Interfaces ---
class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

# --- Concrete Fly Behaviors ---
class Fly(FlyBehavior):
    def fly(self):
        print("Fly")

class NoFly(FlyBehavior):
    def fly(self):
        print("NoFly")


# --- Concrete Quack Behaviors ---
class Quack(QuackBehavior):
    def quack(self):
        print("Quack")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("MuteQuack")


# --- Abstract Duck ---
class Duck(ABC):
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def swim(self):
        print("All ducks float.")

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self, fb: FlyBehavior):
        self.fly_behavior = fb

    def set_quack_behavior(self, qb: QuackBehavior):
        self.quack_behavior = qb

    @abstractmethod
    def display(self):
        pass


# --- Concrete Duck ---
class MallardDuck(Duck):
    def __init__(self):
        super().__init__(Fly(), Quack())

    def display(self):
        print("I'm a Mallard Duck")


# --- Extra Fly Behavior ---
class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")


# --- Demo ---
if __name__ == "__main__":
    model = MallardDuck()
    model.perform_fly()     # Fly
    model.perform_quack()   # Quack
    # Switch behavior at runtime
    model.set_fly_behavior(FlyRocketPowered())
    model.perform_fly()     # I'm flying with a rocket!
