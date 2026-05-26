from abc import ABC, abstractmethod

class ATMState(ABC):
    @abstractmethod
    def insert_card(self, atm):
        pass
    @abstractmethod
    def enter_pin(self,atm):
        pass
    @abstractmethod
    def withdraw_money(self, atm, amount):
        pass
    @abstractmethod
    def eject_card(self,atm):
        pass

class NoCard(ATMState):
    def insert_card(self, atm):
        atm.state = HasCard()
        return "Card inserted."
    def enter_pin(self, atm):
        return "Insert card first."
    def withdraw_money(self, atm, amount):
        return "Only when authenticated"
    def eject_card(self,atm):
        return "No card in ATM"
class HasCard(ATMState):
    def insert_card(self, atm):
        return "Card already insterted."
    def enter_pin(self, atm):
        pin = int(input("Enter PIN:"))
        if pin == atm.pin:
            atm.state = Authenticated()
            return "PIN OK. Authenticated"
        else:
            atm.attempts += 1
            if atm.attempts >= 3:
                atm.state = Blocked()
                return "Wrong PIN. ATM Blocked! Call the bank."
            return "Wrong PIN. Try again."

    def withdraw_money(self, atm, amount):
        return "Only when authenticated"
    def eject_card(self,atm):
        atm.state = NoCard()
        return "Card out."
class Authenticated(ATMState):
    def insert_card(self, atm):
        return "Already authenticated."
    def enter_pin(self, atm):
        return "PIN already entered."
    def withdraw_money(self, atm, amount):
        atm.balance -= amount
        return f"New balance: {atm.balance}"
    def eject_card(self, atm):
        atm.state = NoCard()
        return "Card out."

class Blocked(ATMState):
    def insert_card(self, atm):
        return "CARD BLOCKED"
    def enter_pin(self, atm):
        return "CARD BLOCKED"
    def withdraw_money(self, atm, amount):
        return "CARD BLOCKED"
    def eject_card(self, atm):
        return "CARD BLOCKED"

# BANK AUTOMATA
class ATM:
    def __init__(self):
        self.state = NoCard()
        self.pin = 1234
        self.balance = 50000
        self.attempts = 0
    def button_card(self):
        return self.state.insert_card(self)
    def button_pin(self):
        return self.state.enter_pin(self)
    def button_withdraw(self, amount):
        return self.state.withdraw_money(self, amount)
    def button_eject_card(self):
        return self.state.eject_card(self)

atm = ATM()
print(atm.button_card())
print(atm.button_pin())
print(atm.button_withdraw(5000))
print(atm.button_eject_card())
print(atm.button_pin())
print(atm.button_card())
print(atm.button_withdraw(1000))
print(atm.button_pin())
print(atm.button_withdraw(1000))
print(atm.button_eject_card())
print(atm.button_card())
print(atm.button_pin())
print(atm.button_withdraw(1000))
print(atm.button_withdraw(1000))