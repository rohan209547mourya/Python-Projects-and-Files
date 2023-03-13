account_number = 0


class Account:
    def __init__(self, account_holder_name, opening_balance):
        self.account_number = account_number + 1
        self.holder_name = account_holder_name
        self.balance_amount = opening_balance

    def __str__(self):
        return f"Holder Name : {self.holder_name} \nCurrent balance : {self.balance_amount}"

    def deposit(self, deposit_amount):
        self.balance_amount += deposit_amount
        print(f"Rs.{deposit_amount} deposited successfully!")

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance_amount:
            print("Insufficient Balance")
            return
        self.balance_amount -= withdraw_amount
        print("Withdraw successful")


my_account = Account("Rohan Mourya", 1000)

print(my_account)

my_account.withdraw(1001)

my_account.deposit(1)

my_account.withdraw(1001)
