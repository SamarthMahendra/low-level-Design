# Receiver
class Light:
    def on(self): print("Light is ON")
    def off(self): print("Light is OFF")

# Command interface
class Command:
    def execute(self): pass

# Concrete command
class LightOnCommand(Command):
    def __init__(self, light): self.light = light
    def execute(self): self.light.on()

# Invoker (Remote)
class RemoteControl:
    def __init__(self):
        self.command = None
    def set_command(self, command): self.command = command
    def press_button(self): self.command.execute()

# Usage
light = Light()
light_on = LightOnCommand(light)

remote = RemoteControl()
remote.set_command(light_on)
remote.press_button()  # 👉 Light is ON
