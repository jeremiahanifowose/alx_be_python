# main-0.py

from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Starting with $100
    print("Welcome to your Bank Account!")
    print("Available commands: deposit, withdraw, display, quit")

    while True:
        command = input("\nEnter a command: ").strip().lower()

        if command == "deposit":
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif command == "withdraw":
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif command == "display":
            account.display_balance()

        elif command == "quit":
            print("Goodbye!")
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
