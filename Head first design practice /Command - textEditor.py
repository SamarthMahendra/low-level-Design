

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class Document:
    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text += text

    def erase(self, length):
        self.text = self.text[:-length]

    def __str__(self):
        return self.text

class WriteCommand(Command):
    def __init__(self, document, text):
        self.document = document
        self.text = text

    def execute(self):
        self.document.write(self.text)

    def undo(self):
        self.document.erase(len(self.text))

class EraseCommand(Command):
    def __init__(self, document, length):
        self.document = document
        self.length = length
        self.erased_text = ""

    def execute(self):
        self.erased_text = self.document.text[-self.length:]
        self.document.erase(self.length)

    def undo(self):
        self.document.write(self.erased_text)

class TextEditor:
    def __init__(self):
        self.document = Document()
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()


# --- Demo ---
if __name__ == "__main__":
    editor = TextEditor()

    cmd1 = WriteCommand(editor.document, "Hello, ")
    editor.execute_command(cmd1)
    print(editor.document)  # Output: Hello,

    cmd2 = WriteCommand(editor.document, "World!")
    editor.execute_command(cmd2)
    print(editor.document)  # Output: Hello, World!

    editor.undo()
    print(editor.document)  # Output: Hello,

    cmd3 = EraseCommand(editor.document, 3)
    editor.execute_command(cmd3)
    print(editor.document)  # Output: Hello,

    editor.undo()
    print(editor.document)  # Output: Hello,
