# bank_account.py
import sys

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance (default 0)."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${int(amount)}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account if funds are sufficient."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            print(f"Withdrew: ${int(amount)}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        """Show the current account balance."""
        print(f"Current Balance: ${int(self.__account_balance)}")


def run_checker_mode(account, args):
    """Run in non-interactive mode (used by ALX checkers)."""
    command, *params = args[0].split(':')
    amount = int(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
    elif command == "withdraw" and amount is not None:
        account.withdraw(amount)
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")


def run_interactive_mode(account):
    """Run in interactive mode (for manual testing)."""
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


def main():
    account = BankAccount(100)  # start with $100

    if len(sys.argv) > 1:
        run_checker_mode(account, sys.argv[1:])
    else:
        run_interactive_mode(account)


if __name__ == "__main__":
    main()

