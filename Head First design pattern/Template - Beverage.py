from abc import ABC, abstractmethod

class CaffeineBeverage(ABC):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

    @abstractmethod
    def brew(self): ...

    @abstractmethod
    def add_condiments(self): ...

class Tea(CaffeineBeverage):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")

class Coffee(CaffeineBeverage):
    def brew(self):
        print("Dripping coffee through filter")

    def add_condiments(self):
        print("Adding sugar and milk")


tea = Tea()
coffee = Coffee()

print("Making tea...")
tea.prepare_recipe()

print("\nMaking coffee...")
coffee.prepare_recipe()

