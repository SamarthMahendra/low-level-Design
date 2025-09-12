from abc import ABC, abstractmethod


class GumballMachineRemote(ABC):
    @abstractmethod
    def get_location(self): pass

    @abstractmethod
    def get_count(self): pass


class GumballMachine(GumballMachineRemote):
    def __init__(self, location, count):
        self.location = location
        self.count = count

    def get_location(self):
        return self.location

    def get_count(self):
        return self.count

    def __str__(self):
        return f"GumballMachine[{self.location}]: {self.count} gumballs"

class GumballMachineProxy(GumballMachineRemote):
    def __init__(self, location, server_stub):
        self.location = location
        self.server_stub = server_stub   # Simulated remote reference

    def get_location(self):
        print(f"Proxy: contacting server for {self.location}")
        return self.server_stub.get_location()

    def get_count(self):
        print(f"Proxy: contacting server for {self.location}")
        return self.server_stub.get_count()

class GumballMonitor:
    def __init__(self, machine: GumballMachineRemote):
        self.machine = machine

    def report(self):
        print("---- Machine Report ----")
        print("Location:", self.machine.get_location())
        print("Count:", self.machine.get_count())


# Real machines (could be remote servers)
boston_server = GumballMachine("Boston", 5)
ny_server = GumballMachine("New York", 2)

# Proxies (clients in central office)
boston_proxy = GumballMachineProxy("Boston", boston_server)
ny_proxy = GumballMachineProxy("New York", ny_server)

# Central monitor doesn’t care if it’s a proxy or real
monitor1 = GumballMonitor(boston_proxy)
monitor2 = GumballMonitor(ny_proxy)

monitor1.report()
monitor2.report()
