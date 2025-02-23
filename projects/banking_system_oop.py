'''
📌 Features in the Menu-Based System
✔ Create an account
✔ Deposit money
✔ Withdraw money
✔ Check balance
✔ Exit the system

'''

class BankAccount:
    def __init__(self, account_holder, pin, balance=0.0):
        """Initialize account with holder name, PIN, and balance"""
        self.account_holder = account_holder
        self.pin = pin  # Secure PIN for authentication
        self.balance = balance
        self.transaction_history = []  # Store transactions

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
            print(f"✅ Deposit successful! New balance: {self.balance}")
        else:
            print("❌ Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            print(f"✅ Withdrawal successful! New balance: {self.balance}")
        else:
            print("❌ Insufficient balance or invalid amount.")

    def check_balance(self):
        """Display the current balance"""
        print(f"\n💳 Account Holder: {self.account_holder}")
        print(f"💰 Current Balance: {self.balance}\n")

    def show_transaction_history(self):
        """Display all transactions"""
        print(f"\n📜 Transaction History for {self.account_holder}:")
        if self.transaction_history:
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

# 🏦 Main Banking System
accounts = {}  # Dictionary to store multiple accounts

def create_account():
    """Creates a new bank account"""
    name = input("Enter your name: ").strip()  # Remove extra spaces
    if not name:  # Ensure the name isn't empty after stripping
        print("❌ Name cannot be empty!")
        return
    
    pin = input("Set a 4-digit PIN: ").strip()  # Strip spaces from PIN
    if not pin.isdigit() or len(pin) != 4:  # Ensure PIN is 4-digit number
        print("❌ PIN must be a 4-digit number!")
        return
    
    try:
        initial_deposit = float(input("Enter initial deposit: ").strip())  # Convert input safely
        if initial_deposit < 0:
            print("❌ Deposit amount must be non-negative.")
            return
    except ValueError:
        print("❌ Invalid amount! Please enter a number.")
        return

    accounts[name] = BankAccount(name, pin, initial_deposit)
    print(f"✅ Account created successfully for {name}!")

def login():
    """Authenticate user and access banking features"""
    name = input("\nEnter your name: ").strip()  # Remove extra spaces
    if name in accounts:
        pin = input("Enter your PIN: ").strip()  # Remove spaces from PIN
        if accounts[name].pin == pin:
            print(f"✅ Login successful! Welcome, {name}.")
            account_menu(accounts[name])
        else:
            print("❌ Incorrect PIN. Access Denied!")
    else:
        print("❌ No account found with this name!")

def account_menu(account):
    """Displays the banking menu for an authenticated user"""
    while True:
        print("\n🏦 Banking Menu:")
        print("1️⃣ Deposit Money")
        print("2️⃣ Withdraw Money")
        print("3️⃣ Check Balance")
        print("4️⃣ Transaction History")
        print("5️⃣ Logout")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter deposit amount: ").strip())
                account.deposit(amount)
            except ValueError:
                print("❌ Invalid amount! Please enter a number.")
        elif choice == "2":
            try:
                amount = float(input("Enter withdrawal amount: ").strip())
                account.withdraw(amount)
            except ValueError:
                print("❌ Invalid amount! Please enter a number.")
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.show_transaction_history()
        elif choice == "5":
            print("✅ Logged out successfully!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1-5.")

# Main menu
def main():
    while True:
        print("\n🏦 Welcome to the Secure Banking System:")
        print("1️⃣ Create Account")
        print("2️⃣ Login")
        print("3️⃣ Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("✅ Thank you for using the Banking System! Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1-3.")

# Run the banking system
main()
