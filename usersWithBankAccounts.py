class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.c_Account = Checking
        self.s_Account = Savings

    def deposit(self, amount):
        self.c_Account += amount
        self.s_Account += amount

    def withdraw(self, amount):
        self.c_Account -= amount
        self.s_Account -= amount

    def display_account_info(self):
        print(f"{self.name} Balance: ${self.c_Account.balance}")
        print(f"{self.name} Balance: ${self.s_Account.balance}")
        return self

class BankAccount:
    def __init__(self, name, int_rate, balance):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= 2000:
            self.balance -= amount
        else:
            self.balance -= 5
            print(f"Insufficient funds: Charging a $5 fee, ${self.balance}")
        return self

    def yield_interest(self):
        self.int_rate *= self.balance
        self.balance -= self.int_rate
        return self

    def display_account_info(self):
        print(f"{self.name} Balance: ${self.balance}")
        return self

Checking=BankAccount("Checking", 0.05, 2500)
Savings=BankAccount("Savings", 0.025, 0)

Paymon = User("Paymon", "pkay@gmail.com")
Romin = User("Romin", "rkay@gmail.com")
Sherry = User("Sherry", "skay@hotmail.com")

Paymon.c_Account.deposit(100).deposit(400).withdraw(300).display_account_info()
Paymon.s_Account.deposit(1000).deposit(1500).withdraw(500).withdraw(100).withdraw(100).withdraw(2000).yield_interest().display_account_info()