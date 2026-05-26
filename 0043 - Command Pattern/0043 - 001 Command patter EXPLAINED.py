class Device:
    def behaviour_one(self):
        print("Something happens 1-1.")
    def behaviour_two(self):
        print("Something happens 1-2.")

class BehaviourOne:
    def __init__(self, device):
        self.device = device
    def execute(self):
        self.device.behaviour_one()

class BehaviourTwo:
    def __init__(self, device):
        self.device = device
    def execute(self):
        self.device.behaviour_two()

class RemoteControl:
    def set_command(self,behaviour):
        self.behaviour = behaviour
    def press_button(self):
        self.behaviour.execute()

device = Device()
b1 = BehaviourOne(device)
b2 = BehaviourTwo(device)

remote = RemoteControl()
remote.set_command(b1)
remote.press_button()

remote.set_command(b2)
remote.press_button()