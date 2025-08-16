"""
OOP Practice Problem

Task:
1. Create a base class `BankAccount` with attributes: account_number, account_holder, and balance.
   - Implement methods: deposit(amount), withdraw(amount), and __str__() for printing account details.
2. Create a subclass `SavingsAccount` that inherits from BankAccount and adds:
   - An attribute interest_rate (in %).
   - A method add_interest() that increases the balance based on the interest rate.
3. Create another subclass `CheckingAccount` that:
   - Adds an attribute overdraft_limit.
   - Overrides withdraw(amount) to allow overdraft up to the limit.
4. Demonstrate polymorphism by writing a function that takes any account type and prints its details using __str__().
"""

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds.")

    def __str__(self):
        return (
            f"Account Number: {self.account_number}\n"
            f"Account Holder: {self.account_holder}\n"
            f"Balance: {self.balance:.2f}"
        )


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += (self.interest_rate / 100) * self.balance

    def __str__(self):
        return f"{super().__str__()}\nInterest Rate: {self.interest_rate}%"


class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
        else:
            raise ValueError("Overdraft limit exceeded.")

    def __str__(self):
        return f"{super().__str__()}\nOverdraft Limit: {self.overdraft_limit:.2f}"


# Polymorphism demonstration
def print_account_details(account):
    print(account)  # Automatically calls __str__()


# Example usage
b = BankAccount(121, "Amruta", 10000)
s = SavingsAccount(122, "Amruta", 1000, 10)
c = CheckingAccount(123, "Amruta", 1000, 500)

s.add_interest()
c.withdraw(1200)  # allowed because of overdraft

print_account_details(b)
print()
print_account_details(s)
print()
print_account_details(c)

