# atm.py
class ATM:
    def __init__(self, pin, balance):
        self.correct_pin = pin
        self.balance = balance

    def verify_pin(self, input_pin):
        return input_pin == self.correct_pin

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid amount"
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return "Withdraw successful"

