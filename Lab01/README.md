# 🏧 ATM Mini Project – Nhập Môn Công Nghệ Phần Mềm (PTIT HCM)

## 📘 Giới thiệu dự án
Dự án **ATM Mini Project** mô phỏng hệ thống máy rút tiền tự động (ATM) – được phát triển xuyên suốt qua các **Lab từ 01 → 10**, áp dụng đầy đủ các bước trong quy trình phát triển phần mềm.

**Mục tiêu chính:**
- Xây dựng ứng dụng ATM cơ bản (Login, Withdraw, Check Balance).  
- Thiết kế UML, CSDL, giao diện và kiểm thử tự động.  
- Quản lý tiến độ theo mô hình Scrum và báo cáo trên Jira.  

## 📁 Cấu trúc thư mục
├── Lab01/ # Giới thiệu & setup ban đầu
├── Lab02/ # Use Case Diagram
├── Lab03/ # Sequence Diagram
├── Lab04/ # Form Login (HTML/CSS/JS)
├── Lab05/ # ERD + Database Design
├── Lab06/ # Class & Package Diagram
├── Lab07/ # Withdraw Module + Database
├── Lab08/ # Unit Test + Selenium Test
├── Lab09/ # Jira Sprint Report
└── Lab10-final-demo/ # Báo cáo tổng hợp & demo cuối kỳ

## 🧩 Tổng hợp nội dung từng Lab

| **Lab** | **Nội dung chính** | **File / Đường dẫn** |
|----------|--------------------|------------------------|
| **Lab01** | Giới thiệu bản thân, môi trường làm việc | [Lab01/README.md](./Lab01/README.md) |
| **Lab02** | Phân tích Use Case ATM | [Lab02/usecase_lab02.png](./Lab02/usecase_lab02.png) |
| **Lab03** | Thiết kế Sequence Diagram | [Lab03/sequence_lab03.png](./Lab03/sequence_lab03.png) |
| **Lab04** | Xây dựng giao diện Login | [Lab04/index.html](./Lab04/index.html) |
| **Lab05** | Thiết kế cơ sở dữ liệu (ERD) | [Lab05/project_report.md](./Lab05/project_report.md) |
| **Lab06** | Class & Package Diagram | [Lab06/class_lab06.png](./Lab06/class_lab06.png) |
| **Lab07** | Module Withdraw + DB | [Lab07/withdraw.py](./Lab07/withdraw.py) |
| **Lab08** | Kiểm thử (Unit, Integration, Selenium) | [Lab08/report.md](./Lab08/report.md) |
| **Lab09** | Báo cáo Jira (Scrum, Sprint) | [Lab09/report.md](./Lab09/report.md) |
| **Lab10** | Báo cáo tổng hợp + Demo cuối kỳ | [Lab10-final-demo/final_report.md](./Lab10-final-demo/final_report.md) |

## ⚙️ Chức năng chính của ATM Mini Project

- 🔐 **Đăng nhập (Login):** xác thực người dùng từ DB  
- 💰 **Rút tiền (Withdraw):** trừ tiền & ghi vào lịch sử giao dịch  
- 📄 **Xem số dư / Giao dịch:** đọc dữ liệu từ DB  
- 🧪 **Kiểm thử:**  
  - Unit Test: kiểm tra logic rút tiền  
  - Selenium: mô phỏng đăng nhập trên trình duyệt  
- 📊 **Jira Board:** quản lý nhiệm vụ theo Scrum  

## 💻 Hướng dẫn chạy project

### 1️⃣ Cài đặt môi trường
```bash
pip install selenium
pip install pytest

### 2️⃣ Chạy test tự động
bash
python Lab08/selenium_test_login.py
python Lab08/test_withdraw.py
### 3️⃣ Kết nối Database
Import file SQL: Lab07/atm_demo_dtb.sql vào SQLite hoặc MySQL.
Đảm bảo file db.py trỏ đúng đến database trước khi chạy.

🧠 Công nghệ sử dụng
Thành phần	Công nghệ
Giao diện	HTML, CSS, JavaScript
Xử lý logic	Python
Cơ sở dữ liệu	SQLite
Kiểm thử	Selenium, UnitTest
Quản lý dự án	Jira, GitHub
Báo cáo	Markdown, PowerPoint

🧾 Demo và Kết quả cuối kỳ
🔹 Chạy Form Login → hiển thị “Login successful!”
🔹 Thực hiện Withdraw → cập nhật số dư & lưu lịch sử
🔹 Test thành công các case chính (login, withdraw, balance)
🔹 Jira Board hoàn thiện đầy đủ Sprint và Backlog

📎 Liên kết
GitHub Repository: https://github.com/n23dcpt006-nbin/NMCNPM-ATM
