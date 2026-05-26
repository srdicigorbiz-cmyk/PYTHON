from abc import ABC, abstractmethod

class OrderState(ABC):
    @abstractmethod
    def pay(self, order):
        pass
    @abstractmethod
    def ship(self, order):
        pass

class New(OrderState):
    def pay(self, order):
        order.state = Paid()
        return "State: Paid"
    def ship(self,order):
        return "Pay first"
class Paid(OrderState):
    def pay(self, order):
        return "Already payed"
    def ship(self, order):
        order.state = Shipped()
        return "State: Shiped"
class Shipped(OrderState):
    def pay(self, order):
        return "Already payed and shiped"
    def ship(self, order):
        return "Already payed and shiped"

class Order:
    def __init__(self):
        self.state = New()
    def pay(self):
        return self.state.pay(self)
    def ship(self):
        return self.state.ship(self)

ord = Order()
print(ord.pay())
print(ord.ship())