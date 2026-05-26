from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount

class Bank:
    def __init__(self, name):
        # TODO: Initialize bank with name
        # TODO: Store name as self.name
        # TODO: Initialize empty dictionary for accounts as self.accounts
        self.name = name
        self.accounts = dict()
    
    def create_account(self, account_type, account_number, owner_name, initial_balance=0, **kwargs):
        # TODO: Check if account_number already exists in self.accounts
        # TODO: If exists, return (False, "Account number already exists")
        # TODO: Check account_type (case-insensitive)
        # TODO: If "savings", create SavingsAccount with parameters and **kwargs
        # TODO: If "checking", create CheckingAccount with parameters and **kwargs
        # TODO: If invalid type, return (False, "Invalid account type")
        # TODO: Store account in self.accounts with account_number as key
        # TODO: Return (True, f"{account_type.title()} account created successfully")
        pass
    
    def get_account(self, account_number):
        # TODO: Return account from self.accounts dictionary using account_number as key
        # TODO: Use .get() method to return None if account doesn't exist
        pass
    
    def transfer(self, from_account_number, to_account_number, amount):
        # TODO: Get from_account and to_account using get_account method
        # TODO: Check if both accounts exist
        # TODO: If either account not found, return (False, "One or both accounts not found")
        # TODO: Try to withdraw amount from from_account
        # TODO: If withdrawal fails, return (False, f"Transfer failed: {message}")
        # TODO: If withdrawal succeeds, deposit amount to to_account
        # TODO: Return (True, f"Transferred ${amount:.2f} from {from_account_number} to {to_account_number}")
        pass