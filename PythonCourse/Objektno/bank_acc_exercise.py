class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def get_balance(self):
        return self.balance

    def deposit(self, dep_ammount):
        self.balance += dep_ammount
        return self.balance

    def withdraw(self, withdraw_ammount):
        self.balance -= withdraw_ammount
        return self.balance


acct = BankAccount("Darcy")
print(acct.owner)  # Darcy
print(acct.balance)  # 0.0
print(acct.deposit(10))  # 10.0
print(acct.withdraw(3))  # 7.0
print(acct.get_balance())  # 7.0


