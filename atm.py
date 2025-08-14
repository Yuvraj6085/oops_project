class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def authenticate(self, entered_pin):
        return self.pin == entered_pin

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ₹{amount}")
            print(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print(" Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transactions.append(f"Withdrew ₹{amount}")
                print(f" Withdrew ₹{amount}. New Balance: ₹{self.balance}")
            else:
                print(" Insufficient balance.")
        else:
            print(" Invalid withdrawal amount.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")
        self.transactions.append("Balance Inquiry")

    def view_transactions(self):
        if self.transactions:
            print("\nTransaction History:")
            for t in self.transactions:
                print("-", t)
        else:
            print("No transactions yet.")


atm = ATM(pin=1234, balance=5000)
entered_pin = int(input("Enter PIN: "))
if atm.authenticate(entered_pin):
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Balance Inquiry\n4. Transaction History\n5. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == "3":
            atm.check_balance()
        elif choice == "4":
            atm.view_transactions()
        elif choice == "5":
            print("👋 Thank you for using the ATM.")
            break
        else:
            print("Invalid choice.")
else:
    print("Incorrect PIN.")
