# Target interface
class Duck:
    def quack(self): ...
    def fly(self): ...

# Adaptee
class Turkey:
    def gobble(self): print("Gobble gobble")
    def fly(self): print("I'm flying a short distance")

# Adapter
class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self): self.turkey.gobble()
    def fly(self):
        # Turkeys fly short, so call multiple times
        for _ in range(5):
            self.turkey.fly()

# Usage
def test_duck(duck: Duck):
    duck.quack()
    duck.fly()

turkey = Turkey()
turkey_adapter = TurkeyAdapter(turkey)

test_duck(turkey_adapter)
