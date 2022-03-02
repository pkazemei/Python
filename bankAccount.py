# Create a BankAccount class with the attributes interest rate and balance
class BankAccount:
    def __init__(self, name, int_rate, balance): 
        self.name=name
        self.int_rate=int_rate
        self.balance=balance

# Add a deposit method to the BankAccount class
    def deposit(self, amount):
        self.balance+=amount
        return self

# Add a withdraw method to the BankAccount class
    def withdraw(self, amount):
        if self.balance>=2000:
            self.balance-=amount
        else: 
            self.balance-=5
            print(f"Insufficient funds: Charging a $5 fee, ${self.balance}")
        return self

# Add a yield_interest method to the BankAccount class
    def yield_interest(self):
        self.int_rate*=self.balance
        self.balance-=self.int_rate
        return self

# Add a display_account_info method to the BankAccount class
    def display_account_info(self):
        print(f"{self.name} Balance: ${self.balance}")
        return self

# Create 2 accounts
Checking=BankAccount("Checking", 0.05, 2500)
Savings=BankAccount("Savings", 0.025, 0)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display 
# the account's info all in one line of code (i.e. chaining)
Checking.deposit(100).deposit(100).deposit(400).withdraw(300).display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, 
# then yield interest and display the account's info all in one line of code (i.e. chaining)
Savings.deposit(1000).deposit(1500).withdraw(500).withdraw(100).withdraw(100).withdraw(2000).yield_interest().display_account_info()
