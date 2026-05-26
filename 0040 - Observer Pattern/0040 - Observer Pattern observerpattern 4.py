class Penztar:
    def __init__(self):
        self._subscribers = []
        self.account = 0
    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)
    def account_change(self, value):
        self.account += value
        self.notify(self.account)
    def notify(self, message):
        for sub in self._subscribers:
            sub.update(self.account)


class NaplozóNotifier:
    def update(self, account):
        print(f"Egyenleg: {account}")

class FigyelmeztetesNotifier:
    def update(self, account):
        if account < 0:
            print(f"Egyenleg minuszban van: {account}")


penztar = Penztar()
naplo = NaplozóNotifier()
figyelmeztes = FigyelmeztetesNotifier()

penztar.subscribe(naplo)
penztar.subscribe(figyelmeztes)

penztar.account_change(100)
penztar.account_change(-150)