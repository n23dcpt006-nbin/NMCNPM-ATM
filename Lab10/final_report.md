# Mini Project ATM – Final Report (Lab10)

## 1️. Giới thiệu dự án
**Tên dự án:** ATM Mini Project  
**Mục tiêu:**  
Xây dựng một ứng dụng mô phỏng hệ thống máy rút tiền tự động (ATM) bao gồm các chức năng:
- Đăng nhập người dùng  
- Kiểm tra số dư  
- Rút tiền / Gửi tiền  
- Lưu lịch sử giao dịch  
- Kết nối cơ sở dữ liệu  
- Kiểm thử và báo cáo Sprint theo mô hình Scrum  

**Công cụ sử dụng:**
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python (Flask / SQLite)  
- **Test:** Selenium, Unit Test  
- **Quản lý dự án:** Jira  
- **Thiết kế UML:** Draw.io, Visual Paradigm  
- **Quản lý mã nguồn:** GitHub 

## 2️. Mô hình UML

### Use Case Diagram (Lab02)
![Use Case Diagram](./Lab02/usecase_lab02.png)

[Chi tiết mô tả Use Case](./Lab02/Use%20Case%20Description)

### Sequence Diagram (Lab03)
![Sequence Diagram](./Lab03/sequence_lab03.png)

[Chi tiết mô tả Sequence](./Lab03/Sequence%20Description)

### Class Diagram (Lab06)
![Class Diagram](./Lab06/class_lab06.png)
![Package Diagram](./Lab06/package_lab06.png)

[Ghi chú chi tiết](./Lab06/Notes)

## 3️. Cơ sở dữ liệu (Database)

### ERD + SQL Script (Lab05 & Lab07)
Cấu trúc cơ sở dữ liệu được thiết kế để quản lý người dùng, tài khoản và lịch sử giao dịch.

| Bảng | Mô tả |
|------|--------|
| users | Lưu thông tin người dùng (username, password, balance) |
| transactions | Ghi nhận lịch sử rút/gửi tiền |
| logs | Nhật ký đăng nhập |

File SQL mẫu: [`atm_demo_dtb.sql`](./Lab07/atm_demo_dtb.sql)

## 4️. Giao diện và mã nguồn chính

### Form Login (Lab04)
- File: [`index.html`](./Lab04/index.html)
- Giao diện đăng nhập kết nối với cơ sở dữ liệu để xác thực người dùng.  
- **Frontend:** HTML + CSS + JavaScript.  
- **Mô phỏng chức năng:** Hiển thị thông báo “Login successful” hoặc “Sai thông tin”.

### Withdraw Module (Lab07)
- File chính: [`withdraw.py`](./Lab07/withdraw.py)  
- Kết nối đến cơ sở dữ liệu để trừ số dư, ghi nhận lịch sử rút tiền.  
- Có thêm các module phụ:
  - `check_balance.py`
  - `deposit.py`
  - `transaction_history.py`
  - `db.py`
  - `main.py`  

## 5️. Kiểm thử và Báo cáo Sprint

### Test (Lab08)
- Unit test & integration test:  
  - [`unit_test.png`](./Lab08/unit_test.png)
  - [`integration_test.png`](./Lab08/integration_test.png)
- Selenium test: [`selenium_test_login.py`](./Lab08/selenium_test_login.py)
- Kết quả:
  - ✅ Login thành công khi nhập đúng thông tin
  - ✅ Thông báo lỗi khi sai username/password
  - ✅ Withdraw kiểm tra đúng logic rút tiền

### 📊 Jira Report (Lab09)
| Hạng mục | Hình ảnh minh hoạ |
|-----------|------------------|
| Backlog | ![Backlog](./Lab09/Backlog.png) |
| Sprint board | ![Sprint Board](./Lab09/Sprintboard.png) |
| Burndown chart | ![Burndown](./Lab09/Burndown.png) |
| Tasks chi tiết | ![Tasks](./Lab09/Phân%20rã%20thành%20Tasks/US1%20Rut%20tien.png) |

[Báo cáo Jira chi tiết](./Lab09/report.md)

## 6️. Demo và Kết quả chạy

### Demo các bước
1. **Login:** nhập tài khoản → hiển thị thông báo “Login successful”.  
2. **Withdraw:** nhập số tiền → hệ thống trừ số dư trong DB → ghi log vào bảng `transactions`.  
3. **Kiểm tra test:** chạy `selenium_test_login.py` và `test_withdraw.py`.  
4. **Trình bày Jira:** thể hiện quy trình Scrum và các Sprint trong Lab09.  

## 7️. Kết luận & Định hướng mở rộng

### Kết luận
- Hoàn thiện mô hình mini ATM từ phân tích – thiết kế – cài đặt – kiểm thử.  
- Tích hợp các kỹ thuật phần mềm và công cụ quản lý hiện đại.  

### Định hướng mở rộng
- Thêm module **chuyển khoản giữa các tài khoản**.  
- Xây dựng **giao diện web động** bằng Flask hoặc React.  
- Bổ sung **API RESTful** để dễ mở rộng với mobile app.  
- Áp dụng **CI/CD** (GitHub Actions) để tự động kiểm thử & triển khai.

## Thông tin nộp bài
- **Link GitHub:**  https://github.com/n23dcpt006-nbin/NMCNPM-ATM/tree/main
