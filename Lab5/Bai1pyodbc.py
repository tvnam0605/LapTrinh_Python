import pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server}; Server=ADMIN\SQLEXPRESS;DATABASE=QLSinhVien;UID=sa,PWD=sa,Encrypy=no')
cursor = conn.cursor()
cursor.execute("SELECT @@version")
conn.close()
db_version = cursor.fetchone()
print("Bạn đang dùng hệ quản trị CSDL SQL Server phiên bản ", db_version)
