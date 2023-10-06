import mysql.connector

# Kết nối đến cơ sở dữ liệu MySQL
conn = mysql.connector.connect(user='root', password='123456', host='localhost', database='qlsinhvien')

# Tạo đối tượng cursor
cursor = conn.cursor()

# Thực hiện truy vấn và lấy kết quả
cursor.execute("SELECT @@version")
db_version = cursor.fetchone()[0]
print("Bạn đang sử dụng hệ quản trị CSDL SQL Server phiên bản", db_version)

# Đóng kết nối
conn.close()
