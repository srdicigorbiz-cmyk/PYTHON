class EuroSocket:
    def connect_euro(self):
        return "Európai csatlakozás"
    def disconnect_euro(self):
        return "Európai lecsatlakozva."
class AmericanSocket:
    def connect_usa(self):
        return "Ameriaki csatlakozás"
    def disconnect_usa(self):
        return "Amerikai lekapcsolva."
class Adapter:
    def __init__(self, amerikai_socket):
        self.amerikai_socket = amerikai_socket
    def connect_euro(self):
        return self.amerikai_socket.connect_usa()
    def disconnect_euro(self):
        return self.amerikai_socket.disconnect_usa()

euro = EuroSocket()
amcsi = AmericanSocket()
adapter = Adapter(amcsi)    


print(adapter.connect_euro())
