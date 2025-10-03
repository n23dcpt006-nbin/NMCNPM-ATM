# atm.py
class ATM:
    def __init__(self, balance: float, pin: str):
        self.balance = balance
        self.pin = pin

    def verify_pin(self, input_pin: str) -> bool:
        return self.pin == input_pin

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Invalid withdraw amount")
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
