# Írj egy Allat osztályt és egy Kutya gyereket
# Allat: __init__(nev, kor), __str__: "Név: X, Kor: Y"
# Kutya: örököl, + fajta attribútum, felülírja __str__-t: "Név: X, Kor: Y, Fajta: Z"
# Kutya: + ugat() metódus: "{nev} ugat!"
class Allat:
    def __init__(self, nev, kor):
        self.nev = nev
        self.kor = kor
    def __str__(self):
        return f"Név: {self.nev}, Kor: {self.kor}"
class Kutya(Allat):
    def __init__(self, nev, kor, fajta):
        super().__init__(nev, kor)
        self.fajta = fajta
    def __str__(self):
        return f"Név: {self.nev}, Kor: {self.kor} Fajta: {self.fajta}"
    def ugat (self):
        print(f"{self.nev} ugat!")

k = Kutya("Rex", 3, "Husky")
print(k)
print(k.ugat())