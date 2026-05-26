# Írj egy Beallitasok Singleton osztályt
# - nyelv = "magyar"
# - tema = "vilagos"
class Beallitasok:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self):
        if not hasattr(self, "nyelv"):
            self.nyelv = "magyar"
        if not hasattr(self, "tema"):
            self.tema = "vilagos"


b1 = Beallitasok()
b1.nyelv = "angol"
b2 = Beallitasok()
print(b2.nyelv)    # "angol"
print(b1 is b2)    # True
print(b2.tema)     # "vilagos"