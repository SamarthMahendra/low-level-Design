from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum, auto

class Size(Enum):
    TALL = auto(); GRANDE = auto(); VENTI = auto()

# Component
class Beverage(ABC):
    def __init__(self, description="Unknown Beverage", size: Size = Size.TALL):
        self._description = description
        self._size = size

    def get_description(self) -> str:
        return self._description

    def get_size(self) -> Size:
        return self._size

    @abstractmethod
    def cost(self) -> float: ...

# Concrete components
class Espresso(Beverage):
    def __init__(self, size=Size.TALL):
        super().__init__("Espresso", size)

    def cost(self) -> float:
        base = 1.99
        if self._size == Size.GRANDE: base += 0.20
        elif self._size == Size.VENTI: base += 0.40
        return base

class HouseBlend(Beverage):
    def __init__(self, size=Size.TALL):
        super().__init__("House Blend Coffee", size)

    def cost(self) -> float:
        base = 0.89
        if self._size == Size.GRANDE: base += 0.15
        elif self._size == Size.VENTI: base += 0.30
        return base

class DarkRoast(Beverage):
    def __init__(self, size=Size.TALL):
        super().__init__("Dark Roast Coffee", size)

    def cost(self) -> float:
        base = 0.99
        if self._size == Size.GRANDE: base += 0.15
        elif self._size == Size.VENTI: base += 0.30
        return base

class Decaf(Beverage):
    def __init__(self, size=Size.TALL):
        super().__init__("Decaf Coffee", size)

    def cost(self) -> float:
        base = 1.05
        if self._size == Size.GRANDE: base += 0.15
        elif self._size == Size.VENTI: base += 0.30
        return base

# Decorator base
class CondimentDecorator(Beverage, ABC):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    # condiments inherit size from wrapped beverage
    def get_size(self) -> Size:
        return self._beverage.get_size()

    @abstractmethod
    def get_description(self) -> str: ...

# Concrete decorators
def soy_price(size: Size) -> float:
    return {Size.TALL: 0.10, Size.GRANDE: 0.15, Size.VENTI: 0.20}[size]

class Soy(CondimentDecorator):
    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Soy"

    def cost(self) -> float:
        return self._beverage.cost() + soy_price(self.get_size())

class Mocha(CondimentDecorator):
    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Mocha"

    def cost(self) -> float:
        return self._beverage.cost() + 0.20

class Whip(CondimentDecorator):
    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Whip"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10

class Milk(CondimentDecorator):
    def get_description(self) -> str:
        return f"{self._beverage.get_description()}, Milk"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10

# Usage (same flows as the book)
if __name__ == "__main__":
    # Straight Espresso
    b1 = Espresso()
    print(b1.get_description(), f"${b1.cost():.2f}")

    # DarkRoast + Mocha + Mocha + Whip
    b2 = DarkRoast()
    b2 = Mocha(b2)
    b2 = Mocha(b2)
    b2 = Whip(b2)
    print(b2.get_description(), f"${b2.cost():.2f}")

    # HouseBlend (VENTI) + Soy + Mocha + Whip
    b3 = HouseBlend(size=Size.VENTI)
    b3 = Soy(b3)
    b3 = Mocha(b3)
    b3 = Whip(b3)
    print(b3.get_description(), f"${b3.cost():.2f}")
