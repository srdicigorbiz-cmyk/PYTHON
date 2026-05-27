from account import Account
from transaction import Transaction

class CheckingAccount(Account):
    def __init__(self, account_number, owner_name, balance=0, overdraft_limit=100):
        # TODO: Call parent constructor with account_number, owner_name, and balance
        # TODO: Store overdraft_limit as self.overdraft_limit (default 100)
        super().__init__(account_number, owner_name, balance)
        self.overdraft_limit = overdraft_limit
        
    def withdraw(self, amount):
        # TODO: Validate that amount is positive (> 0)
        # TODO: If invalid, return (False, "Withdrawal amount must be positive")
        # TODO: Check if withdrawal would exceed overdraft limit
        # TODO: If exceeds limit, return (False, f"Cannot exceed overdraft limit of ${self.overdraft_limit:.2f}")
        # TODO: Subtract amount from self.balance
        # TODO: Create Transaction object with "withdrawal", amount, and self
        # TODO: Append transaction to self.transaction_history
        # TODO: If balance is negative, return message with "(Overdraft)" suffix
        # TODO: Otherwise return normal withdrawal message
        # TODO: Format: (True, f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        if amount > 0:
            if amount > self.overdraft_limit+self.balance:
                return (False, f"Cannot exceed overdraft limit of ${self.overdraft_limit:.2f}")
            else:
                self.balance -= amount
                transaction = Transaction("withdrawal", amount, self)
                self.transaction_history.append(transaction)
                if self.balance < 0:
                    return (True, f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f} (Overdraft)")
                else:
                    return (True, f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

        else:
            return (False, "Withdrawal amount must be positive")