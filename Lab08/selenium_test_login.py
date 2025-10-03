from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time, sys

URL = "file:///D:/nguynbin/NHAP-MON-CNPM/NMCNPM-ATM/NMCNPM-ATM/Lab04/index.html"

try:
    driver = webdriver.Chrome()
except Exception as e:
    print("ERROR: ChromeDriver not found")
    sys.exit(1)

driver.get(URL)
time.sleep(1)

# === Test case 1: Login đúng ===
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(0.5)

# ✅ Xử lý alert "Login successful!"
alert = Alert(driver)
assert alert.text == "Login successful!"
alert.accept()   # bấm OK
print("✅ Test 1 (Login success) passed")

# === Test case 2: Sai password ===
driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(0.5)

msg = driver.find_element(By.ID, "error-msg").text.strip()
print("DEBUG msg =", repr(msg))
assert msg == "The Username or Password is incorrect!"
print("✅ Test 2 (Wrong password) passed")

# === Test case 3: Input trống ===
driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "password").clear()
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(0.5)

msg = driver.find_element(By.ID, "error-msg").text.strip()
assert msg == "Please enter full your Username and Password!"
print("✅ Test 3 (Empty input) passed")

driver.quit()
