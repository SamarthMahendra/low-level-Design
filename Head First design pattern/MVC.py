class Model:
    def __init__(self):
        self.count = 0
        self.observers = []

    def increment(self):
        self.count += 1
        self.notify_observers()

    def get_count(self):
        return self.count

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for o in self.observers:
            o.update(self)


class View:
    def update(self, model):
        print(f"[View] Count is now: {model.get_count()}")


class Controller:
    def __init__(self, model):
        self.model = model

    def handle_button_click(self):
        self.model.increment()



model = Model()
view = View()
controller = Controller(model)

# View observes the model
model.register_observer(view)

# Simulate button clicks
controller.handle_button_click()
controller.handle_button_click()
