# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance (default 0)."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account if funds are sufficient."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        """Show the current account balance."""
        print(f"Current Balance: ${self.__account_balance}")


def main():
    account = BankAccount(100)  # starting with $100

    while True:
        command = input("\nEnter command (deposit, withdraw, display, quit): ").strip().lower()

        if command == "deposit":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif command == "withdraw":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif command == "display":
            account.display_balance()

        elif command == "quit":
            print("Goodbye!")
            break

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()


