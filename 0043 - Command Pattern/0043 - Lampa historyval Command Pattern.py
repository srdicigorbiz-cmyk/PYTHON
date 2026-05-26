from abc import ABC, abstractmethod

# Receiver: Ő tudja, hogyan kell világítani
class Light:
    def on(self):
        print("A lámpa felkapcsolva.")
    
    def off(self):
        print("A lámpa lekapcsolva.")

# Command Interfész
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

# Invoker: A távirányító
class RemoteControl:
    def __init__(self):
        self.command = None
        self.history = [] # Az Undo-hoz

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()
        self.history.append(self.command)

    def press_undo(self):
        if self.history:
            cmd = self.history.pop()
            cmd.undo()

# Használat
lamp = Light()
on_cmd = LightOnCommand(lamp)

remote = RemoteControl()
remote.set_command(on_cmd)

remote.press_button() # Kimenet: A lámpa felkapcsolva.
remote.press_undo()   # Kimenet: A lámpa lekapcsolva.