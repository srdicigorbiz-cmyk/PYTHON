from abc import ABC, abstractmethod
from transaction import Transaction

class Account(ABC):
    def __init__(self, account_number, owner_name, balance=0):
        # TODO: Initialize account with account_number, owner_name, and balance
        # TODO: Store account_number as self.account_number
        # TODO: Store owner_name as self.owner_name
        # TODO: Store balance as self.balance (default 0)
        # TODO: Initialize empty list for transaction_history as self.transaction_history
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.transaction_history = []

    
    def deposit(self, amount):
        # TODO: Validate that amount is positive (> 0)
        # TODO: If invalid, return (False, "Deposit amount must be positive")
        # TODO: Add amount to self.balance
        # TODO: Create Transaction object with "deposit", amount, and self
        # TODO: Append transaction to self.transaction_history
        # TODO: Return (True, f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        if amount > 0:
            self.balance += amount
            transaction = Transaction("deposit", amount, self)
            self.transaction_history.append(transaction)
            return (True, f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            return (False, "Deposit amount must be positive")
    
    @abstractmethod
    def withdraw(self, amount):
        # TODO: Abstract method - must be implemented by concrete account classes
        # TODO: Should handle withdrawal logic specific to account type
        # TODO: Should return tuple (success_boolean, message_string)
        pass
    
    def get_balance(self):
        # TODO: Return the current balance
        return self.balance
    
    def get_transaction_history(self):
        # TODO: Return the transaction_history list
        return self.transaction_history