# bank_account.py

# 🏦 Bank Account Simulation using OOP in Python

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("Total balance = ", self.get_balance())

    def credited(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("Total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance


# Sample usage
if __name__ == "__main__":
    acc1 = Account(100000000, 1234)
    acc1.debit(20000)
    acc1.credited(520000)
