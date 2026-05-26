class CreditCard:
    def pay(self, amount):
        return f"Paid ${amount} with Credit Card"

class PayPal:
    def pay(self, amount):
        return f"Paid ${amount} with PayPal"

class Bitcoin:
    def pay(self, amount):
        return f"Paid ${amount} with Bitcoin"
    
class ShoppingCart:
    def __init__(self):
        self.total = 0
        self.payment_strategy = None
    
    def add_item(self, price):
        self.total += price
    
    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy
    
    def checkout(self):
        return self.payment_strategy.pay(self.total)
    
cart = ShoppingCart()
cart.add_item(50)
cart.add_item(30)

# Use credit card strategy
cart.set_payment_strategy(CreditCard())
print(cart.checkout())

# Switch to PayPal strategy
cart.set_payment_strategy(PayPal())
print(cart.checkout())