# Írj egy Naplo Singleton osztályt
# - level = "INFO" (alapértelmezett)
# - barmikor hívod, ugyanazt az objektumot adja vissza
class Naplo:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def __init__(self):
        if not hasattr(self, "level"):
            self.level = "INFO"

n1 = Naplo()
n1.level = "ERROR"
n2 = Naplo()
print(n2.level)   # "ERROR"
print(n1 is n2)   # True