# Van: EmailKuldes, SmsKuldes, PushKuldes osztályok
# Mindegyiknek: kuld(uzenet) metódusa
# Van: Ertesito context osztály
# + legyen set_strategia() metódus is a csere helyett
class EmailKuldes:
    def kuld(self, uzenet):
        return f"Email: {uzenet}"
class SmsKuldes:
    def kuld(self, uzenet):
        return f"SMS: {uzenet}"
class PushKuldes:
    def kuld(self, uzenet):
        return f"Push: {uzenet}"

class Ertesito:
    def __init__(self, strategia):
        self.strategia = strategia
    def set_strategia (self, strategia):
        self.strategia = strategia
    def kuld(self, uzenet):
        return self.strategia.kuld(uzenet)
    
e = Ertesito(EmailKuldes())
print(e.kuld("Helló!"))

e.set_strategia(SmsKuldes())
print(e.kuld("Helló!"))

e.set_strategia(PushKuldes())
print(e.kuld("Helló!"))