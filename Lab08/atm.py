# atm.py
"""
Simple ATM module for lab.
Functions:
- verify_pin(accounts, acc_id, pin) -> bool
- withdraw(accounts, acc_id, amount) -> bool or raises ValueError
accounts is a dict: { acc_id: {"pin": "1234", "balance": 1000}, ... }
"""
from typing import Dict

def verify_pin(accounts: Dict, acc_id: str, pin: str) -> bool:
    """Return True if acc_id exists and pin matches, else False."""
    if acc_id not in accounts:
        return False
    return accounts[acc_id].get("pin") == pin

def withdraw(accounts: Dict, acc_id: str, amount: float) -> bool:
    """
    Try to withdraw amount from account.
    - If account not found -> raise ValueError
    - If amount invalid (<=0) -> raise ValueError
    - If enough balance -> subtract and return True
    - If not enough -> return False (no change)
    """
    if acc_id not in accounts:
        raise ValueError("Account not found")
    if amount <= 0:
        raise ValueError("Invalid withdraw amount")
    balance = accounts[acc_id].get("balance", 0)
    if balance >= amount:
        accounts[acc_id]["balance"] = balance - amount
        return True
    else:
        return False
if __name__ == "__main__":
    accounts = {
        "acc1": {"pin": "1234", "balance": 1000},
        "acc2": {"pin": "0000", "balance": 50},
    }

    print(verify_pin(accounts, "acc1", "1234"))   # True
    print(verify_pin(accounts, "acc1", "1111"))   # False

    print(withdraw(accounts, "acc1", 200))        # True
    print(accounts["acc1"]["balance"])            # 800

    print(withdraw(accounts, "acc2", 100))        # False
    print(accounts["acc2"]["balance"])            # 50
