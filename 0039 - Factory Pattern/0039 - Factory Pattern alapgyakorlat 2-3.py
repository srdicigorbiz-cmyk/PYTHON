# Írj egy AlkalmazottFactory-t
# - Fejleszto, Tesztelo, Manager osztályok
# - mindegyiknek: szerep() metódus
# - Factory dictionary alapú, raise ValueError
class Fejleszto:
    def szerep(self):
        return "Fejleszto"
class Tesztelo:
    def szerep(self):
        return "Tesztelo"
class Manager:
    def szerep(self):
        return "Manager"
class AlkalmazottFactory:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "lista"):
            self.lista={
                "fejleszto": Fejleszto,
                "tesztelo": Tesztelo,
                "manager": Manager
            }
    def letrehoz(self, cls):
        if cls.lower() in self.lista:
            return self.lista[cls.lower()]()
        else:
            raise ValueError("ismeretlen")



f = AlkalmazottFactory()
print(f.letrehoz("fejleszto").szerep())
print(f.letrehoz("manager").szerep())
print(f.letrehoz("könyvelő").szerep())  # ValueError!