from db import get_connection

def get_transaction_history(account_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE account_id = %s", (account_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows
