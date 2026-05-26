class BankAccount:
    def __init__(self):
        self._subscribers = []
    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)
        return "Subscriber added."
    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)
    def notify(self, message):
        for sub in self._subscribers:
            sub.update(message)

class AppNotifier:
    def update(self, message):
        print(message)

class EmailNotifier:
    def update(self, message):
        print(message)
class SmsNotifier:
    def update(self, message):
        print(message)