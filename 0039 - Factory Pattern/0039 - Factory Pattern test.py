# Van: Espresso, Latte, Cappuccino osztály
# __init__: meret ("kis", "közepes", "nagy")
# leiras() metódus: "Kis espresso készül..."
class Espresso:
    def __init__(self, meret):
        self.meret = meret
    def leiras(self):
        return f"{self.meret} espresso készül..."
class Latte:
    def __init__(self, meret):
        self.meret = meret
    def leiras(self):
        return f"{self.meret} latte készül..."
class Cappucino:
    def __init__(self, meret):
        self.meret = meret
    def leiras(self):
        return f"{self.meret} cappucino készül..."
# KaveFactory:
# - dictionary alapú
# - letrehoz(tipus, meret) metódus
class KaveFactory:
    def __init__(self):
        self.lista={
            "espresso" : Espresso,
            "latte" : Latte,
            "capuccino" : Cappucino
        }
    def letrehoz(self, cls, meret):
        if cls in self.lista:
            return self.lista[cls](meret)
        else:
            raise ValueError("Hibas!")
# Teszteld:
factory = KaveFactory()
print(factory.letrehoz("espresso", "kis").leiras())
print(factory.letrehoz("latte", "nagy").leiras())