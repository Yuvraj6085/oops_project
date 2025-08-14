class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print(" Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f" Withdrawn ₹{amount}. New balance: ₹{self.balance}")
            else:
                print(" Insufficient balance.")
        else:
            print(" Invalid withdrawal amount.")

    def check_balance(self):
        print(f"Account Balance: ₹{self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=4.0):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest added: ₹{interest}. New balance: ₹{self.balance}")


class CurrentAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=5000):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                print(f" Withdrawn ₹{amount}. New balance: ₹{self.balance}")
            else:
                print(" Overdraft limit exceeded.")
        else:
            print(" Invalid withdrawal amount.")
savings = SavingsAccount("S123", "Vinit Sharma", 10000)
current = CurrentAccount("C456", "Yuvraj Sharma", 5000)
savings.deposit(2000)
savings.add_interest()
savings.withdraw(3000)
savings.check_balance()

print("\n---\n")
current.deposit(1500)
current.withdraw(8000)
current.check_balance()
