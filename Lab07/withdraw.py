from db import get_connection

def withdraw(account_id, amount):
    conn = get_connection()
    cursor = conn.cursor()

    # Lấy số dư hiện tại
    cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (account_id,))
    balance = cursor.fetchone()[0]

    if balance >= amount:
        # Trừ tiền
        new_balance = balance - amount
        cursor.execute("UPDATE accounts SET balance = %s WHERE account_id = %s",
                       (new_balance, account_id))
        # Lưu vào transactions
        cursor.execute("INSERT INTO transactions (account_id, card_no, amount) VALUES (%s, %s, %s)",
                       (account_id, None, -amount))
        conn.commit()
        conn.close()
        return True, new_balance
    else:
        conn.close()
        return False, balance