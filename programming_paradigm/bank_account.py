# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if funds are sufficient."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.__account_balance}")

