class Bankszamla:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self):
        if not hasattr(self, "observers"):
            self.observers=[]
    def subscribe(self, observer):
        self.observers.append(observer)
    def notify(self):
        if len(self.observers)>0:
            for o in self.observers:
                o.update()
    def unsubscribe(self, observer):
        self.observers.remove(observer)

class EmailErtesito:
    def update(self):
        print("Email értesítés elküldve!")
class SmsErtesito:
    def update(self):
        print("SMS értesítés")
############################################
bankszamla = Bankszamla()
emailertesit = EmailErtesito()
smsertesit = SmsErtesito()

###########################################
bankszamla.subscribe(emailertesit)
bankszamla.subscribe(smsertesit)
bankszamla.notify()

bankszamla.unsubscribe(emailertesit)
bankszamla.notify()