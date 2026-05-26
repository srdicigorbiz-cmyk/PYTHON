# Van: Pizza, Burger, Sushi osztályok
# Mindegyiknek: leiras() metódusa
# Van: EtelFactory – dictionary alapú, raise ValueError
class Pizza:
    def leiras(self):
        return "Ez egy pizza."

class Burger:
    def leiras(self):
        return "Ez egy burger."

class Sushi:
    def leiras(self):
        return "Ez egy sushi."

class EtelFactory:
    def __init__(self):
        self.etelfajtak = {
            "pizza" : Pizza,
            "burger": Burger,
            "sushi" : Sushi
        }

    def letrehoz(self, etel):
        if etel.lower() in self.etelfajtak:
            return self.etelfajtak[etel.lower()]()
        else:
            raise ValueError("Ilyen étel nincs!")
        



f = EtelFactory()
print(f.letrehoz("pizza").leiras())
print(f.letrehoz("burger").leiras())
print(f.letrehoz("hotdog").leiras())  # ValueError!