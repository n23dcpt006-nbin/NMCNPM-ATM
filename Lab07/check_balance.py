from db import get_connection

def check_balance(account_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (account_id,))
    balance = cursor.fetchone()
    conn.close()
    if balance:
        return balance[0]
    else:
        return None
