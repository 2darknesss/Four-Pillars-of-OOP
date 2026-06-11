# Encapsulation: bundling data and methods, hiding the balance (__balance).
# Direct external access is restricted; state can only be modified via safe methods.
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Double underscore makes the attribute private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
account.withdraw(20)
print(account.get_balance())
