# Írj egy AppBeallitas Singleton osztályt
# - nyelv = "magyar", tema = "vilagos", verzio = "1.0"
# - bármikor hívod, ugyanazt az objektumot adja vissza
class AppBeallitas:
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
        if not hasattr(self, "verzio"):
            self.verzio = "1.0"

b1 = AppBeallitas()

b1.nyelv = "angol"
b1.tema = "sotet"

b2 = AppBeallitas()
print(b2.nyelv)   # "angol"
print(b2.tema)    # "sotet"
print(b2.verzio)  # "1.0"
print(b1 is b2)   # True