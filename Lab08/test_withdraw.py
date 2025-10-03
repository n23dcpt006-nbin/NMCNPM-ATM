# test_withdraw.py
import pytest
from atm import ATM

def test_verify_pin_correct():
    atm = ATM(1000, "1234")
    assert atm.verify_pin("1234") == True

def test_verify_pin_incorrect():
    atm = ATM(1000, "1234")
    assert atm.verify_pin("0000") == False

def test_withdraw_success():
    atm = ATM(1000, "1234")
    result = atm.withdraw(500)
    assert result == True
    assert atm.balance == 500

def test_withdraw_insufficient():
    atm = ATM(300, "1234")
    result = atm.withdraw(500)
    assert result == False
    assert atm.balance == 300
