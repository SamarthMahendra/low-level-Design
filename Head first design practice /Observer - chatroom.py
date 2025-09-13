

from typing import Protocol, List, runtime_checkable, Optional


@runtime_checkable
class Observer(Protocol):
    def update(self, text: str) -> None:
        ...

@runtime_checkable
class Subject(Protocol):
    def subscribe(self, obs: Observer) -> None: ...
    def unsubscribe(self, obs: Observer) -> None: ...
    def notify(self, message: str) -> None: ...


class User(Observer):

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, text: str) -> None:
        print(f"[{self.name}'s screen] {text}")



class ChatRoom(Subject):

    def __init__(self):
        self._observers = []

    def subscribe(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
        else:
            print(f"Observer {getattr(observer, 'name', observer)} not registered")

    def post_message(self, message: str) -> None:
        self.notify(message)

    def notify(self, message) -> None:
        for observer in list(self._observers):
            observer.update(message)


room = ChatRoom()

alice = User("Alice")
bob = User("Bob")
carol = User("Carol")

room.subscribe(alice)
room.subscribe(bob)

room.post_message("Welcome to the chat!")
# Alice and Bob get this message

room.unsubscribe(bob)
room.post_message("Only Alice should see this")
# Carol not subscribed yet, Bob unsubscribed, only Alice sees






