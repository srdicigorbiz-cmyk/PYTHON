class Transaction:
    def __init__(self, transaction_type, amount, account):
        # TODO: Initialize transaction with transaction_type, amount, and account
        # TODO: Store transaction_type as self.transaction_type
        # TODO: Store amount as self.amount
        # TODO: Store account as self.account
        self.transaction_type = transaction_type
        self.amount = amount
        self.account = account
    
    def __str__(self):
        # TODO: Return formatted string representation of the transaction
        # TODO: Format: "{self.transaction_type.title()} - ${self.amount:.2f}"
        # TODO: Use .title() to capitalize first letter of transaction_type
        return f"{self.transaction_type.title()} - ${self.amount:.2f}"