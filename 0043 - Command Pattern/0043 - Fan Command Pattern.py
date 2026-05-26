# Van: Fan (ventillátor) osztály - start(), stop() metódusokkal
# Van: FanStartCommand, FanStopCommand – execute() és undo()
# Van: RemoteControl – set_command(), press_button()
class Fan:
    def start(self):
        print("Fan started.")
    def stop(self):
        print("Fan stoped.")
class FanStartCommand:
    def __init__(self, device):
        self.device = device
    def execute(self):
        self.device.start()
    def undo(self):
        self.device.stop()
class FanStopCommand:
    def __init__(self, device):
        self.device = device
    def execute(self):
        self.device.stop()
    def undo(self):
        self.device.start()
class RemoteControl:
    def set_command(self, command):
        self.command = command
    def press_button(self):
        self.command.execute()
        

fan = Fan()
remote = RemoteControl()

remote.set_command(FanStartCommand(fan))
remote.press_button()

remote.set_command(FanStopCommand(fan))
remote.press_button()