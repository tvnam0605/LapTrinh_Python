import mysql.connector
from prettytable import PrettyTable

# user = 'root'
# password = '123456'
# host = 'localhost'
# database = 'qlsinhvien'

def get_connection():
    conn = mysql.connector.connect(user='root', password='123456', host='localhost', database='qlsinhvien')
    return conn

def close_connection(conn):
    if conn:
        conn.close()

def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = "SELECT * FROM Lop"
        cursor.execute(select_query)

        records = cursor.fetchall()

        print(f"Danh sách các lớp là: ")
        for row in records:
            print("*" * 50)
            print("Mã lớp: ", row[0])
            print("Tên lớp: ", row[1])
        
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

def get_all_sv():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """
        SELECT SinhVien.ID AS 'Mã số', SinhVien.HoTen AS 'Họ tên', 
               SinhVien.MaLop AS 'Mã lớp', Lop.TenLop AS 'Tên lớp'
        FROM SinhVien
        LEFT JOIN Lop ON SinhVien.MaLop = Lop.ID
        """
        
        cursor.execute(select_query)
        records = cursor.fetchall()

        table = PrettyTable()
        table.field_names = ["Mã số", "Họ tên", "Mã lớp", "Tên lớp"]

        print("Danh sách tất cả các sinh viên là: ")
        for row in records:
            table.add_row([row[0], row[1], row[2], row[3]])

        print(table)
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

#get_all_sv()

def get_class_by_id(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = "SELECT * FROM Lop WHERE id = %s"

        #  sử dụng tuple để truyền tham số
        params = (class_id,)
        cursor.execute(select_query, params)

        records = cursor.fetchall()

        if len(records) > 0:
            print(f"Thông tin lớp có id = {class_id} là: ")
            print("Mã lớp: ", records[0][0])
            print("Tên lớp: ", records[0][1])
        else:
            print(f"Không tìm thấy lớp có id = {class_id}")

        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

#get_class_by_id(1)

def get_student_by_id(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query="Select * from SinhVien where ID = %s"

        params =(student_id,)
        cursor.execute(select_query, params)

        records = cursor.fetchall()
        
        if len(records) > 0:
            print(f"Thông tin sinh viên có mã số {student_id} là: ")
            print("Mã số: ", records[0][0])
            print("Họ tên: ", records[0][1])
            print("Mã lớp: ", records[0][2])
        else:
            print(f"Không tìm thấy sinh viên có mã số {student_id}")

        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)
#get_student_by_id(1)

# hiện thị danh sách sinh viên theo mã lớp/tên lớp
def get_student_by_idclass(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query ="Select * from SinhVien where MaLop = %s"

        params =(class_id,)
        cursor.execute(select_query,params)

        records = cursor.fetchall()

        table = PrettyTable()
        table.field_names = ["Mã số", "Họ tên", "Mã lớp"]

        print(f"Danh sách sinh viên có mã lớp {class_id} là: ")
        for row in records:
            table.add_row([row[0], row[1], row[2]])

        print(table)
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

#get_student_by_idclass(2)
# tìm kiếm thông tin theo tên và lớp
def search_student_by_name_class(name, class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        select_query = "SELECT * FROM SinhVien WHERE HoTen LIKE %s AND MaLop = %s"

        #thêm '%' vào biến name để tìm kiếm theo tên chứa phần tử name
        params = (f"%{name}%", class_id,)
        cursor.execute(select_query,params)   

        records = cursor.fetchall()  
        table = PrettyTable()
        table.field_names = ["Mã số", "Họ tên", "Mã lớp"]

        print(f"Sinh viên tên {name} có mã lớp {class_id} là: ")
        for row in records:
            table.add_row([row[0], row[1], row[2]])

        print(table)
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)
#search_student_by_name_class("Trung", 3)

# insert/Update/Delete
def insert_class(class_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Tạo giá trị ID bằng cách tự tạo
        insert_query = "INSERT INTO Lop ( TenLop) VALUES (%s)"
        data = (class_name,)
        cursor.execute(insert_query, data)

        connection.commit()

        print("Đã thêm thành công!")

        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

insert_class("MTK45")


# hàm thêm sinh viên
def insert_student(name, class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.callproc('InsertStudent',(name, class_id,))

        # thay đổi vào csdl
        connection.commit()
        print(f"Đã thêm thành công sinh viên có tên {name}, mã lớp {class_id}  vào bảng sinh viên")
        get_all_sv()
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)
#insert_student("Trần Văn Nam", 2)
# Sửa sinh viên
def edit_student(student_id, new_name, new_class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Gọi thủ tục lưu trữ EditStudent
        cursor.callproc('EditStudent', (student_id, new_name, new_class_id))

        # Commit thay đổi vào cơ sở dữ liệu
        connection.commit()

        print(f"Đã cập nhật thông tin sinh viên thành công!")

        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

# Gọi hàm để sửa thông tin sinh viên bằng thủ tục lưu trữ
#edit_student(13, 'Trần Văn Nam', 1)  # Thay thế thông tin sinh viên theo mã số sinh viên và tên lớp mới

# xóa sinh viên
def delete_student(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.callproc('DeleteStudent',(student_id,))

        connection.commit()

        print(f"Đã xóa thành công sinh viên có mã {student_id} ra khỏi cơ sở dữ liệu!")
        get_all_sv()
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

# delete_student(14)

get_all_class()
