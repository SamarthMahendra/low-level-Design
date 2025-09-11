from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def prepare(self): ...
    def bake(self): print("Baking")
    def cut(self): print("Cutting")
    def box(self): print("Boxing")


# --- New York Style Pizzas ---
class NYCheesePizza(Pizza):
    def prepare(self): print("Preparing NY Style Cheese Pizza")

class NYVeggiePizza(Pizza):
    def prepare(self): print("Preparing NY Style Veggie Pizza")

class NYClamPizza(Pizza):
    def prepare(self): print("Preparing NY Style Clam Pizza")

class NYPepperoniPizza(Pizza):
    def prepare(self): print("Preparing NY Style Pepperoni Pizza")


# --- Chicago Style Pizzas ---
class ChicagoCheesePizza(Pizza):
    def prepare(self): print("Preparing Chicago Style Cheese Pizza")
    def cut(self): print("Cutting Chicago Style Pizza into square slices")  # Chicago quirk

class ChicagoVeggiePizza(Pizza):
    def prepare(self): print("Preparing Chicago Style Veggie Pizza")
    def cut(self): print("Cutting Chicago Style Pizza into square slices")

class ChicagoClamPizza(Pizza):
    def prepare(self): print("Preparing Chicago Style Clam Pizza")
    def cut(self): print("Cutting Chicago Style Pizza into square slices")

class ChicagoPepperoniPizza(Pizza):
    def prepare(self): print("Preparing Chicago Style Pepperoni Pizza")
    def cut(self): print("Cutting Chicago Style Pizza into square slices")


class PizzaStore(ABC):
    def order_pizza(self, type_: str):
        pizza = self.create_pizza(type_)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, type_: str) -> Pizza:
        pass


class NYPizzaStore(PizzaStore):
    def create_pizza(self, type_: str) -> Pizza:
        if type_ == "cheese":
            return NYCheesePizza()
        elif type_ == "veggie":
            return NYVeggiePizza()
        elif type_ == "clam":
            return NYClamPizza()
        elif type_ == "pepperoni":
            return NYPepperoniPizza()
        else:
            raise ValueError("Unknown pizza type")


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, type_: str) -> Pizza:
        if type_ == "cheese":
            return ChicagoCheesePizza()
        elif type_ == "veggie":
            return ChicagoVeggiePizza()
        elif type_ == "clam":
            return ChicagoClamPizza()
        elif type_ == "pepperoni":
            return ChicagoPepperoniPizza()
        else:
            raise ValueError("Unknown pizza type")


ny_store = NYPizzaStore()
chicago_store = ChicagoPizzaStore()

print("\n--- Ordering NY Cheese Pizza ---")
ny_store.order_pizza("cheese")

print("\n--- Ordering Chicago Clam Pizza ---")
chicago_store.order_pizza("clam")

print("\n--- Ordering NY Pepperoni Pizza ---")
ny_store.order_pizza("pepperoni")

print("\n--- Ordering Chicago Veggie Pizza ---")
chicago_store.order_pizza("veggie")
