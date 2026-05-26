# TODO: Import the BankAccount class from bank_account.py
from bank_account import BankAccount

# TODO: Create two accounts with these exact details:
# - account1: holder "Alice Smith" with $1000 balance
# - account2: holder "Bob Jones" with $2000 balance
account1=BankAccount("Alice Smith", 1000)
account2=BankAccount("Bob Jones", 2000)
# TODO: Call display_info() for both accounts
account1.display_info()
account2.display_info()
# TODO: Change the class variable interest_rate to 0.03 (3%)
# Use this format: BankAccount.interest_rate = 0.03
BankAccount.interest_rate=0.03

# TODO: Print the text "After interest rate change:"
print("After interest rate change:")

# TODO: Call display_info() for both accounts again to show they both have the new interest rate
account1.display_info()
account2.display_info()