# Írj egy Adatbazis Singleton osztályt
# - host = "localhost", port = 5432, kapcsolat = False
# - csatlakozas(): kapcsolat = True, kiírja: "Kapcsolódva: {host}:{port}"
# - lecsatlakozas(): kapcsolat = False, kiírja: "Lecsatlakozva"
class Adatbazis:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance
    def __init__(self):
        if not hasattr(self, "host"):
            self.host = "localhost"
        if not hasattr(self, "port"):
            self.port = 5432
        if not hasattr(self, "kapcsolat"):
            self.kapcsolat = False
    def csatlakozas(self):
        self.kapcsolat = True
        return f"Kapcsolódva: {self.host}:{self.port}"
    def lecsatlakozas(self):
        self.kapcsolat = False
        return f"Lecsatlakozva"


db1 = Adatbazis()
db1.csatlakozas()
db1.host = "192.168.1.1"

db2 = Adatbazis()
print(db2.host)       # "192.168.1.1"
print(db2.kapcsolat)  # True
db2.lecsatlakozas()
print(db1.kapcsolat)  # False
print(db1 is db2)     # True