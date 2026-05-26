# Írj egy JarmuFactory-t
# - Auto, Hajó, Repulo osztályok
# - mindegyiknek: tipus() metódus
# - Factory dictionary alapú, raise ValueError
# - case-insensitive
class Auto:
    def tipus(self):
        return "Auto"
class Hajo:
    def tipus(self):
        return "Hajo"
class Repulo:
    def tipus(self):
        return "Repulo"

class JarmuFactory:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "lista"):
            self.lista ={
                "auto": Auto,
                "hajo": Hajo,
                "repulo": Repulo
            }
    def letrehoz(self, cls):
        if cls.lower() in self.lista:
            return self.lista[cls.lower()]()
        else:
            raise ValueError("Ismeretlen.")

f = JarmuFactory()
print(f.letrehoz("auto").tipus())
print(f.letrehoz("HAjo").tipus())
print(f.letrehoz("vonat").tipus())  # ValueError!