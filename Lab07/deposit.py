from db import get_connection

def deposit(account_id, amount):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (account_id,))
    balance = cursor.fetchone()[0]

    new_balance = balance + amount
    cursor.execute("UPDATE accounts SET balance = %s WHERE account_id = %s",
                   (new_balance, account_id))
    cursor.execute("INSERT INTO transactions (account_id, card_no, amount) VALUES (%s, %s, %s)",
                   (account_id, None, amount))
    conn.commit()
    conn.close()
    return new_balance
