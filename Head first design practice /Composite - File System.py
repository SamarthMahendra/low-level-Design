

from abc import ABC, abstractmethod

class FileSystemNode(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def display(self, indent: int = 0) -> None:
        pass


class File(FileSystemNode):

    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size

    def display(self, indent: int = 0) -> None:
        print(" " * indent + f"File: {self.name} (Size: {self.size} bytes)")


class Directory(FileSystemNode):

    def __init__(self, name: str):
        super().__init__(name)
        self.children = []

    def add(self, node: FileSystemNode) -> None:
        self.children.append(node)

    def remove(self, node: FileSystemNode) -> None:
        self.children.remove(node)

    def display(self, indent: int = 0) -> None:
        print(" " * indent + f"Directory: {self.name}")
        for child in self.children:
            child.display(indent + 2)


# --- Demo ---
if __name__ == "__main__":
    root = Directory("root")
    home = Directory("home")
    docs = Directory("docs")

    file1 = File("notes.txt", 1000)
    file2 = File("resume.pdf", 25000)

    docs.add(file1)
    home.add(docs)
    home.add(file2)
    root.add(home)

    root.display()
