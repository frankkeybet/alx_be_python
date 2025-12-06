class BankAccount:
    """Simple bank account that stores a numeric balance."""

    def __init__(self, initial_balance=0.0):
        """
        Initialize an account.
        initial_balance: optional starting balance (default 0.0)
        """
        # Use a private attribute to encourage encapsulation
        self._account_balance = float(initial_balance)
    
    def deposit(self, amount):
        """
        Add money to the account.
        Returns True if deposit succeeded, False if invalid amount.
        """
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            return False

        if amount < 0:
            # don't allow negative deposits
            return False

        self._account_balance += amount
        return True
    

    def withdraw(self, amount):
        """
        Attempt to withdraw amount from account.
        If enough funds, deduct and return True.
        If insufficient funds or invalid amount, return False.
        """
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            return False

        if amount < 0:
            return False

        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        """Prints the current balance in a friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")

    def get_balance(self):
        """Return the current balance as a float."""
        return self._account_balance
    
# main-0.py
import sys
from bank_account import BankAccount

def main():
    # Start with an example balance; you can change this for testing
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # split first argument into command and optional amount
    command_part = sys.argv[1]
    command, *params = command_part.split(':')
    amount = None
    if params and params[0] != '':
        try:
            amount = float(params[0])
        except ValueError:
            print("Invalid amount. Please provide a numeric value.")
            sys.exit(1)

    if command == "deposit" and amount is not None:
        success = account.deposit(amount)
        if success:
            print(f"Deposited: ${amount:.0f}" if amount.is_integer() else f"Deposited: ${amount}")
        else:
            print("Deposit failed: invalid amount.")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.0f}" if amount.is_integer() else f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
