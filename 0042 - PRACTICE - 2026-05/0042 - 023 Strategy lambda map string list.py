class SimaSzovegStrategia:
    def formatum(self, uzenet, *args):   
        return (uzenet + " - " + ' - '.join(list(map(lambda x: str(x), args))))
        

class DiktStrategia:
    def formatum(self, uzenet, *args):
        return {"main":uzenet, "details":list(args)}

class Logger:
    def __init__(self, strategia):
        self.strategia = strategia
    def set_strategia(self, strategia):
        self.strategia = strategia
    def naploz(self, uzenet, *args):
        return self.strategia.formatum(uzenet, *args)


logger = Logger(SimaSzovegStrategia())
print(logger.naploz("Hiba történt", "404", "User: Admin"))
# Elvárt: Hiba történt - 404 - User: Admin

logger.set_strategia(DiktStrategia())
print(logger.naploz("Sikeres mentés", "ID: 102", "200 OK"))
# Elvárt: {'main': 'Sikeres mentés', 'details': ['ID: 102', '200 OK']}


