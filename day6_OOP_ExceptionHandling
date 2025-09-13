# Bank Account System with OOP and Exception Handling

class InsufficientBalanceError(Exception):
    """Custom Exception for low balance"""
    pass

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"✅ {amount} deposited. Current Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("❌ Withdrawal denied! Insufficient balance.")
        self.balance -= amount
        print(f"✅ {amount} withdrawn. Current Balance: {self.balance}")

    def display(self):
        print(f"👤 Account Holder: {self.account_holder}, Balance: {self.balance}")

# Inherited Class
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"💰 Interest of {interest:.2f} added. New Balance: {self.balance:.2f}")

# ---- Testing ----
try:
    acc1 = SavingsAccount("Sanika", 1000)
    acc1.display()
    acc1.deposit(500)
    acc1.withdraw(200)
    acc1.add_interest()
    acc1.withdraw(2000)   # This will raise custom exception
except InsufficientBalanceError as e:
    print(e)
finally:
    print("✅ Transaction Process Completed")
