class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_off()

class Light:
    def turn_on(self):
        print("Light is on")
    
    def turn_off(self):
        print("Light is off")

class RemoteControl:
    def __init__(self):
        self.command = None
    
    def set_command(self, command):
        self.command = command
    
    def press_button(self):
        self.command.execute()

class UndoableCommand(Command):
    def undo(self):
        pass

class LightOnCommand(UndoableCommand):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()
    
    def undo(self):
        self.light.turn_off()

class SmartRemote:
    def __init__(self):
        self.last_command = None
    
    def execute_command(self, command):
        command.execute()
        self.last_command = command
    
    def undo(self):
        if self.last_command:
            self.last_command.undo()



# Create receiver
light = Light()

# Create commands
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

# Create invoker
remote = RemoteControl()

# Execute different commands
remote.set_command(light_on)
remote.press_button()

remote.set_command(light_off)
remote.press_button()

smart_remote = SmartRemote()
smart_remote.execute_command(LightOnCommand(light))
smart_remote.undo()  # Turns light off

