# Create a file with the User class, including the __init__ and make_deposit methods
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

# Add a make_withdrawal method to the User class
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

# Add a display_user_balance method to the User class
    def display_user_balance(self):
        print(self.name, self.account_balance)
        return self

# Create 3 instances of the User class
Paymon = User("Paymon", "pkay@gmail.com")
Romin = User("Romin", "rkay@gmail.com")
Sherry = User("Sherry", "skay@hotmail.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
Paymon.make_deposit(500).make_deposit(250).make_deposit(750).make_withdrawal(1000).display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
Romin.make_deposit(1000).make_deposit(1500).make_withdrawal(1250).make_withdrawal(250).display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
Sherry.make_deposit(800).make_withdrawal(200).make_withdrawal(200).make_withdrawal(400).display_user_balance()