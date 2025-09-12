from abc import ABC, abstractmethod

class Quackable(ABC):
    @abstractmethod
    def quack(self): pass


class MallardDuck(Quackable):
    def quack(self): print("Quack")

class RubberDuck(Quackable):
    def quack(self): print("Squeak")

class DecoyDuck(Quackable):
    def quack(self): print("<< Silence >>")

class Goose:
    def honk(self): print("Honk")

class GooseAdapter(Quackable):
    def __init__(self, goose): self.goose = goose
    def quack(self): self.goose.honk()


class QuackCounter(Quackable):
    count = 0

    def __init__(self, duck: Quackable):
        self.duck = duck

    def quack(self):
        self.duck.quack()
        QuackCounter.count += 1

    @staticmethod
    def get_quacks():
        return QuackCounter.count


class Flock(Quackable):
    def __init__(self):
        self.quackers = []

    def add(self, quacker: Quackable):
        self.quackers.append(quacker)

    def quack(self):
        for q in self.quackers:
            q.quack()



class AbstractDuckFactory(ABC):
    @abstractmethod
    def create_mallard_duck(self): pass
    @abstractmethod
    def create_rubber_duck(self): pass
    @abstractmethod
    def create_decoy_duck(self): pass
    @abstractmethod
    def create_goose(self): pass


class CountingDuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self): return QuackCounter(MallardDuck())
    def create_rubber_duck(self): return QuackCounter(RubberDuck())
    def create_decoy_duck(self): return QuackCounter(DecoyDuck())
    def create_goose(self): return QuackCounter(GooseAdapter(Goose()))


class QuackObserver(ABC):
    @abstractmethod
    def update(self, duck: Quackable): pass


class Quackologist(QuackObserver):
    def update(self, duck: Quackable):
        print(f"[Observer] {duck.__class__.__name__} just quacked!")


class Observable:
    def __init__(self, duck: Quackable):
        self.duck = duck
        self.observers = []

    def register_observer(self, observer: QuackObserver):
        self.observers.append(observer)

    def notify_observers(self):
        for o in self.observers:
            o.update(self.duck)


def simulate():
    factory = CountingDuckFactory()

    mallard = factory.create_mallard_duck()
    rubber = factory.create_rubber_duck()
    decoy = factory.create_decoy_duck()
    goose = factory.create_goose()

    flock = Flock()
    flock.add(mallard)
    flock.add(rubber)
    flock.add(decoy)
    flock.add(goose)

    print("\nDuck Simulator: Whole Flock Simulation")
    flock.quack()

    print("\nTotal quacks counted:", QuackCounter.get_quacks())

