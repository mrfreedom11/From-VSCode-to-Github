class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance  

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            print('Not enough money in your bank account')
            return 0
        else:
            self.balance -= amount
            return amount

    def display_balance(self):
        print(f"Current balance: {self.balance}")

# Obyekt yaratish
account = BankAccount(
    first_name='Sobir',
    last_name='Axmedov',
    account_id=123456,
    account_type='kartadagi pul',
    pin=5555,
    balance=10.0
)

# Amal bajarish
account.deposit(96)
account.withdraw(25)
account.display_balance()
