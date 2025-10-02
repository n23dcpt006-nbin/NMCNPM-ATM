DROP DATABASE atm_demo;
CREATE DATABASE atm_demo;
USE atm_demo;

USE atm_demo;

CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    account_no VARCHAR(20) UNIQUE,
    balance DOUBLE
);

CREATE TABLE cards (
    card_no VARCHAR(20) PRIMARY KEY,
    pin_hash VARCHAR(64),
    status VARCHAR(20),
    account_id INT,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

CREATE TABLE transactions (
    tx_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    card_no VARCHAR(20),
    atm_id INT,
    tx_type VARCHAR(20),
    amount DOUBLE,
    balance_after DOUBLE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);
-- Thêm 1 tài khoản có số dư 5000
INSERT INTO accounts (account_no, balance)
VALUES ('ACC001', 5000);

-- Thêm thẻ liên kết với tài khoản trên
-- PIN: 1234 (mình sẽ lưu dạng chuỗi text bình thường để demo, còn nếu muốn bảo mật có thể hash SHA256)
INSERT INTO cards (card_no, pin_hash, status, account_id)
VALUES ('12345678', '1234', 'active', 1);

-- Kiểm tra dữ liệu
SELECT * FROM accounts;
SELECT * FROM cards;
