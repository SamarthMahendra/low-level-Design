



class Logger:

    _instance = None
    _messages =[]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


    def log(self, message):
        self._messages.append(message)


a = Logger()
b = Logger()

print(a is b)
