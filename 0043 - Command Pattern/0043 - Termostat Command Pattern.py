# Van: Termostat osztály
#   - heat_up(): "Fűtés bekapcsolva"
#   - cool_down(): "Hűtés bekapcsolva"  
#   - off(): "Termostat kikapcsolva"
# Van: HeatCommand, CoolCommand – execute() és undo()
# Van: SmartRemote – execute_command(), undo()
class Termostat:
    def heat_up(self):
        print("Fűtés bekapcsolva")
    def cool_down(self):
        print("Hűtés bekapcsolva")
    def off(self):
        print("Termostat kikapcsolva")

class HeatCommand:
    def __init__(self, device):
        self.device = device
    def execute(self):
        self.device.heat_up()
    def undo(self):
        self.device.off()

class CoolCommand:
    def __init__(self, device):
        self.device = device
    def execute(self):
        self.device.cool_down()
    def undo(self):
        self.device.off()

class SmartRemote:
    def execute_command(self, command):
        self.command = command
        self.command.execute()
    def undo(self):
        self.command.undo()


termostat = Termostat()
remote = SmartRemote()

remote.execute_command(HeatCommand(termostat))
remote.undo()
remote.execute_command(CoolCommand(termostat))
remote.undo()