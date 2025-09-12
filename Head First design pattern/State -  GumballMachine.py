from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def insert_quarter(self): pass
    @abstractmethod
    def eject_quarter(self): pass
    @abstractmethod
    def turn_crank(self): pass
    @abstractmethod
    def dispense(self): pass


class NoQuarterState(State):
    def __init__(self, machine): self.machine = machine

    def insert_quarter(self):
        print("You inserted a quarter")
        self.machine.set_state(self.machine.has_quarter_state)

    def eject_quarter(self):
        print("You haven't inserted a quarter")

    def turn_crank(self):
        print("You turned, but there’s no quarter")

    def dispense(self):
        print("You need to pay first")


class HasQuarterState(State):
    def __init__(self, machine): self.machine = machine

    def insert_quarter(self):
        print("You can't insert another quarter")

    def eject_quarter(self):
        print("Quarter returned")
        self.machine.set_state(self.machine.no_quarter_state)

    def turn_crank(self):
        print("You turned the crank...")
        self.machine.set_state(self.machine.sold_state)
        self.machine.dispense()

    def dispense(self):
        print("No gumball dispensed")


class SoldState(State):
    def __init__(self, machine): self.machine = machine

    def insert_quarter(self):
        print("Please wait, already giving a gumball")

    def eject_quarter(self):
        print("Sorry, you already turned the crank")

    def turn_crank(self):
        print("Turning twice doesn’t give another gumball")

    def dispense(self):
        print("A gumball comes rolling out...")
        self.machine.count -= 1
        if self.machine.count == 0:
            print("Oops, out of gumballs!")
            self.machine.set_state(self.machine.sold_out_state)
        else:
            self.machine.set_state(self.machine.no_quarter_state)


class SoldOutState(State):
    def __init__(self, machine): self.machine = machine

    def insert_quarter(self):
        print("Machine is sold out")

    def eject_quarter(self):
        print("No quarter to return")

    def turn_crank(self):
        print("You turned, but no gumballs")

    def dispense(self):
        print("No gumball dispensed")


class GumballMachine:
    def __init__(self, count: int):
        self.count = count

        # create states
        self.sold_out_state = SoldOutState(self)
        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)

        # initial state
        self.state = self.sold_out_state if count == 0 else self.no_quarter_state

    def set_state(self, state): self.state = state

    # delegate to state
    def insert_quarter(self): self.state.insert_quarter()
    def eject_quarter(self): self.state.eject_quarter()
    def turn_crank(self): self.state.turn_crank()
    def dispense(self): self.state.dispense()


gumball = GumballMachine(2)

gumball.insert_quarter()
gumball.turn_crank()

gumball.insert_quarter()
gumball.turn_crank()

gumball.insert_quarter()
