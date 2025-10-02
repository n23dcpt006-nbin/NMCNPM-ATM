import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # hoặc NguyenBinh nếu bạn đã tạo user đó
        password="CaMau2025", # mật khẩu bạn đã note lại
        database="atm_demo",  # tên database, phải chắc là đã tạo trước
        port=3306             # cổng mặc định
    )
