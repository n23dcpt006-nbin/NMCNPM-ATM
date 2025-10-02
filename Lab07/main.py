import mysql.connector

# ------------------ KẾT NỐI DATABASE ------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="CaMau2025",   # 🔴 đổi thành mật khẩu root MySQL của bạn
    database="atm_demo"
)
cursor = conn.cursor()

ACCOUNT_ID = 1  # dùng tạm account_id = 1

# ------------------ CÁC HÀM CHỨC NĂNG ------------------

# Hàm ghi log giao dịch
def log_transaction(account_id, tx_type, amount, balance_after):
    sql = "INSERT INTO transactions (account_id, tx_type, amount, balance_after) VALUES (%s, %s, %s, %s)"
    val = (account_id, tx_type, amount, balance_after)
    cursor.execute(sql, val)
    conn.commit()

# Kiểm tra số dư
def check_balance(account_id):
    cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (account_id,))
    balance = cursor.fetchone()[0]
    return balance

# Rút tiền
def withdraw(account_id, amount):
    balance = check_balance(account_id)
    if amount > balance:
        print("❌ Not enough balance!")
        return
    new_balance = balance - amount
    cursor.execute("UPDATE accounts SET balance = %s WHERE account_id = %s", (new_balance, account_id))
    conn.commit()
    log_transaction(account_id, "WITHDRAW", amount, new_balance)
    print(f"✅ Withdraw success. New balance: {new_balance}")

# Nạp tiền
def deposit(account_id, amount):
    balance = check_balance(account_id)
    new_balance = balance + amount
    cursor.execute("UPDATE accounts SET balance = %s WHERE account_id = %s", (new_balance, account_id))
    conn.commit()
    log_transaction(account_id, "DEPOSIT", amount, new_balance)
    print(f"✅ Deposit success. New balance: {new_balance}")

# Lịch sử giao dịch
def get_transaction_history(account_id):
    sql = "SELECT tx_type, amount, balance_after, created_at FROM transactions WHERE account_id = %s ORDER BY created_at DESC"
    cursor.execute(sql, (account_id,))
    return cursor.fetchall()

# ------------------ MENU CHÍNH ------------------
def main():
    while True:
        print("\n=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transaction History")
        print("0. Exit")
        choice = input("Choose: ")

        if choice == "1":
            balance = check_balance(ACCOUNT_ID)
            print(f"💰 Balance: {balance}")
        elif choice == "2":
            amount = float(input("Amount to withdraw: "))
            withdraw(ACCOUNT_ID, amount)
        elif choice == "3":
            amount = float(input("Amount to deposit: "))
            deposit(ACCOUNT_ID, amount)
        elif choice == "4":
            history = get_transaction_history(ACCOUNT_ID)
            print("\n--- Transaction History ---")
            for row in history:
                print(row)
        elif choice == "0":
            print("👋 Bye!")
            break
        else:
            print("⚠️ Invalid choice!")

# ------------------ START ------------------
if __name__ == "__main__":
    main()
    cursor.close()
    conn.close()
