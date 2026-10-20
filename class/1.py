class BankAccount:
    count = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.count += 1
        self.account_number = BankAccount.count

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print(self.account_holder, "Balance:", self.balance)

    def transfer(self, amount, other):
        if amount <= self.balance:
            self.balance -= amount
            other.balance += amount
            print("Transfer successful!")
        else:
            print("Insufficient balance!")

a1 = BankAccount("Rahul")
a2 = BankAccount("Priya")

a1.deposit(5000)
a2.deposit(8000)

a1.withdraw(1000)

a1.transfer(2000, a2)

a1.display_balance()
a2.display_balance()
