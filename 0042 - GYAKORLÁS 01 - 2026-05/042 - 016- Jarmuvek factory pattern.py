# Van: Teheruto, Szemelyauto, Motor osztályok
# __init__: rendszam
# leiras(): "Rendszám: X, Típus: Y"
# Van: JarmuFactory – dictionary alapú, raise ValueError
class Teherauto:
    def __init__(self, rendszam):
        self.rendszam = rendszam
        
    def leiras(self):
        return f"Rendszám: {self.rendszam}, Típus: Teherautó"

class Szemelyauto:
    def __init__(self, rendszam):
        self.rendszam = rendszam
        
    def leiras(self):
        return f"Rendszám: {self.rendszam}, Típus: Szemelyauto"

class Motor:
    def __init__(self, rendszam):
        self.rendszam = rendszam
        
    def leiras(self):
        return f"Rendszám: {self.rendszam}, Típus: Motor"
        
class JarmuFactory:
    def __init__(self):
        self.jarmulista = {
        "teherauto": Teherauto,
        "szemelyauto":Szemelyauto,
        "motor": Motor
        }
    def letrehoz(self, tipus, rendszam):
        if tipus in self.jarmulista:
            return self.jarmulista[tipus](rendszam)
        else:
            raise ValueError("Ilyen tipus nincs.")


f = JarmuFactory()
print(f.letrehoz("teherauto", "ABC-123").leiras())
print(f.letrehoz("motor", "XYZ-789").leiras())
print(f.letrehoz("repulo", "DEF-456").leiras())  # ValueError!