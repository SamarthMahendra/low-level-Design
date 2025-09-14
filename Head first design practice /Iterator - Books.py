from abc import ABC, abstractmethod


# --- Iterator Interface ---
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass


# --- Concrete Iterators ---
class ListBookIterator(Iterator):
    def __init__(self, books: list):
        self._books = books
        self._position = 0

    def has_next(self) -> bool:
        return self._position < len(self._books)

    def next(self):
        if not self.has_next():
            raise StopIteration
        book = self._books[self._position]
        self._position += 1
        return book


class DictBookIterator(Iterator):
    def __init__(self, books: dict):
        self._items = list(books.values())
        self._position = 0

    def has_next(self) -> bool:
        return self._position < len(self._items)

    def next(self):
        if not self.has_next():
            raise StopIteration
        book = self._items[self._position]
        self._position += 1
        return book


class SetBookIterator(Iterator):
    def __init__(self, books: set):
        self._items = list(books)  # convert to list for ordered access
        self._position = 0

    def has_next(self) -> bool:
        return self._position < len(self._items)

    def next(self):
        if not self.has_next():
            raise StopIteration
        book = self._items[self._position]
        self._position += 1
        return book


# --- Collection Interfaces ---
class BookCollection(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass


class NewArrivalCollection(BookCollection):
    def __init__(self, books: list):
        self._books = books

    def create_iterator(self) -> Iterator:
        return ListBookIterator(self._books)


class ArchiveCollection(BookCollection):
    def __init__(self, books: dict):
        self._books = books

    def create_iterator(self) -> Iterator:
        return DictBookIterator(self._books)


class ManuscriptCollection(BookCollection):
    def __init__(self, books: set):
        self._books = books

    def create_iterator(self) -> Iterator:
        return SetBookIterator(self._books)


# --- Demo ---
if __name__ == "__main__":
    new_arrivals = NewArrivalCollection(["Book A", "Book B", "Book C"])
    archives = ArchiveCollection({1: "Old Book 1", 2: "Old Book 2"})
    manuscripts = ManuscriptCollection({"Manuscript X", "Manuscript Y"})

    print("\n-- New Arrivals --")
    it = new_arrivals.create_iterator()
    while it.has_next():
        print(it.next())

    print("\n-- Archives --")
    it = archives.create_iterator()
    while it.has_next():
        print(it.next())

    print("\n-- Manuscripts --")
    it = manuscripts.create_iterator()
    while it.has_next():
        print(it.next())
