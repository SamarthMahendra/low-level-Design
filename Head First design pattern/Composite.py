from abc import ABC, abstractmethod

# Common interface
class MenuComponent(ABC):
    @abstractmethod
    def print(self): ...

class MenuItem(MenuComponent):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print(self):
        print(f"  {self.name}: ${self.price}")


class Menu(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, component: MenuComponent):
        self.items.append(component)

    def print(self):
        print(f"\n{self.name}")
        for item in self.items:
            item.print()   # ✅ no type-check needed!



# Build hierarchy
main_menu = Menu("Main Menu")
lunch_menu = Menu("Lunch Menu")
dessert_menu = Menu("Dessert Menu")

lunch_menu.add(MenuItem("BLT Sandwich", 6.99))
lunch_menu.add(MenuItem("Veggie Burger", 7.99))

dessert_menu.add(MenuItem("Apple Pie", 3.99))
dessert_menu.add(MenuItem("Ice Cream", 2.99))

main_menu.add(lunch_menu)
main_menu.add(dessert_menu)

# Print everything
main_menu.print()

