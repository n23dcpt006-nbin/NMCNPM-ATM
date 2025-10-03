# 🏧 Lab 08 – Kiểm thử ATM

## 🎯 Mục tiêu
- Thực hành Unit Test và Integration Test cho module ATM.  
- Sử dụng công cụ **pytest** và **Selenium**.  

---

## 🔹 Unit Test (test_withdraw.py)
- Hàm `verify_pin`: kiểm tra PIN đúng/sai.  
- Hàm `withdraw`: kiểm tra rút tiền thành công/thất bại.  

✅ Kết quả: tất cả test case đều **PASSED**.  
![UnitTest](./Lab08/unit_test.png)

---

## 🔹 Integration Test (selenium_test_login.py)
- **Case 1**: Login đúng → Hiển thị alert `"Login successful!"`.  
- **Case 2**: Sai mật khẩu → `"The Username or Password is incorrect!"`.  
- **Case 3**: Input trống → `"Please enter full your Username and Password!"`.  

✅ Kết quả: cả 3 test đều **PASSED**.  
![Integration Test](.Lab08/integration_test.png)

---

## 📌 Kết luận
- Đã viết **Unit Test** và **Integration Test** cho hệ thống ATM.  
- Tất cả các test case chạy thành công.  
- Lab08 hoàn thành đúng yêu cầu.  
