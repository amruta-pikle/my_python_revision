"""
banking_system.py

Problem Statement:
------------------
Design and implement a simple Banking System using Python Exception Handling
and Custom Exceptions.

Requirements:
1. Create a base class `BankAccount` with attributes:
   - account number
   - account holder name
   - balance

2. Implement methods:
   - deposit(amount): increases balance
   - withdraw(amount): decreases balance if sufficient funds are available
   - get_balance(): returns current balance

3. Create custom exceptions:
   - `InsufficientFundsError` → raised when withdrawal is greater than balance
   - `InvalidAmountError` → raised when deposit or withdrawal amount <= 0

4. Demonstrate exception handling:
   - Handle custom exceptions with try/except blocks
   - Show meaningful error messages when invalid operations are attempted

5. Write a demo program that:
   - Creates a bank account
   - Performs deposits and withdrawals
   - Catches and handles exceptions gracefully
"""

class InsufficientFundsError(Exception):
    """Raised when withdrawal exceeds account balance."""
    pass


class InvalidAmountError(Exception):
    """Raised when an invalid deposit/withdrawal amount is used."""
    pass


class BankAccount:
    def __init__(self, account_number: str, holder_name: str, balance: float = 0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <=0:
            raise InvalidAmountError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be greater than zero.")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}. Available balance: {self.balance}"
            )
        self.balance -= amount
        print(f"Withdrew {amount}. New balace: {self.balance}")
    def get_balance(self) -> float:
        return self.balance

if __name__ == "__main__":
    # Demo usage with try/except blocks
    account = BankAccount("1234", "Amruta",1000)

    try:
        account.deposit(500)
        account.withdraw(200)
        account.withdraw(2000)
    except InvalidAmountError as e:
        print(f"Invalid transaction: {e}")
    except InsufficientFundsError as e:
        print(f"Transaction failed: {e}")


    try:
        account.deposit(-50)
    except InvalidAmountError as e:
        print(f"Invalid transaction: {e}")

    print(f"Final Balance : {account.get_balance()}")
