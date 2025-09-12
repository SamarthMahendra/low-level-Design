class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price}"


class PancakeHouseMenu:  # stored as list
    def __init__(self):
        self.items = []
        self.add_item("Pancake Breakfast", 5.99)
        self.add_item("Regular Pancake", 3.99)

    def add_item(self, name, price):
        self.items.append(MenuItem(name, price))

    def create_iterator(self):
        return iter(self.items)  # Python built-in iterator


class DinerMenu:  # stored as dict
    def __init__(self):
        self.items = {}
        self.add_item("Veggie Burger", 7.99)
        self.add_item("BLT Sandwich", 6.99)

    def add_item(self, name, price):
        self.items[name] = MenuItem(name, price)

    def create_iterator(self):
        return iter(self.items.values())  # dict -> values iterator


def print_menu(menu):
    iterator = menu.create_iterator()
    for item in iterator:
        print(item)

pancake_menu = PancakeHouseMenu()
diner_menu = DinerMenu()

print("Pancake House Menu:")
print_menu(pancake_menu)

print("\nDiner Menu:")
print_menu(diner_menu)

