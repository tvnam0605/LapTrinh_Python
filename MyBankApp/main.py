import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyodbc
from PIL import Image, ImageTk

current_user_info = {}
amount_entries = []

#=============================================Kết nối cơ sở dữ liệu==========================================#
def get_db_connection():
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=.\SQLEXPRESS;"
        "Database=BankDatabase;"
        "Trusted Connection=yes;"
        "UID=sa;"
        "PWD=sa;"
    )
    return conn
def close_connection(conn):
    if conn:
        conn.close()
##=============================================Hàm để lấy FullName từ cơ sở dữ liệu dựa vào UserID==========================================#
def get_full_name_by_user_id(user_id):
    try:
        conn = get_db_connection()  # Hàm kết nối cơ sở dữ liệu của bạn
        cursor = conn.cursor()

        # Thực hiện truy vấn để lấy FullName từ bảng Users dựa vào UserID
        cursor.execute("SELECT FullName FROM Users WHERE UserID=?", (user_id,))
        result = cursor.fetchone()

        if result:
            full_name = result[0]
            return full_name
        else:
            return None

    except Exception as e:
        print("Error:", str(e))
        return None
#=============================================Lấy tên tài khoản dựa vào số tàikhoanr==========================================#
def get_account_name_by_account_number(account_number):
    try:
        # Lấy kết nối đến cơ sở dữ liệu
        conn = get_db_connection()

        # Tạo một đối tượng cursor để thực hiện truy vấn SQL
        cursor = conn.cursor()

        # Truy vấn SQL để lấy tên tài khoản dựa vào số tài khoản
        cursor.execute("SELECT AccountName FROM Accounts WHERE AccountNumber = ?", (account_number,))
        
        # Lấy kết quả
        row = cursor.fetchone()

        if row:
            return row.AccountName  # Trả về tên tài khoản nếu tìm thấy
        else:
            return "Không có tài khoản"  # Trả về thông báo nếu không tìm thấy

    except Exception as e:
        print("Lỗi khi truy vấn cơ sở dữ liệu:", str(e))
        return "Lỗi khi truy vấn cơ sở dữ liệu"
    finally:
        close_connection(conn)
#=============================================Lấy thông tin người dùng==========================================#
def get_user_info(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT Username, Balance FROM Users u JOIN Accounts a ON u.UserID = a.UserID WHERE u.UserID = ?", (user_id,))
        row = cursor.fetchone()
        if row:
            username, balance = row
            return username, balance
        else:
            return None, None
    except Exception as e:
        messagebox.showerror("Lỗi", "Lỗi khi lấy thông tin người dùng: " + str(e))
        return None, None
    finally:
        if conn:
            conn.close()
#=============================================Lấy số dư tài khoản==========================================#
def get_account_balance(user_id):
    try:
        # Lấy kết nối từ hàm get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()

        # Thực hiện truy vấn để lấy số dư của tài khoản
        cursor.execute("SELECT Balance FROM Accounts WHERE UserID = ?", (user_id,))
        row = cursor.fetchone()

        if row:
            balance = row[0]
            return balance
        else:
            return None
    except Exception as e:
        print(str(e))
        return None
    finally:
        close_connection(conn)
#=============================================Lấy user name đang hoạt động==========================================#
def get_current_username():
    if "Tên đăng nhập" in current_user_info:
        return current_user_info["Tên đăng nhập"]
    else:
        return None  # Hoặc bạn có thể trả về một giá trị mặc định khác nếu không tìm thấy tên đăng nhập
#===================================================================================================================#
#=============================================Lấy id dựa vào name đang hoạt động==========================================#
def get_user_id_by_username(username):
    conn = get_db_connection()  # Thay thế hàm này bằng hàm kết nối đến cơ sở dữ liệu của bạn
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT UserID FROM Users WHERE Username=?", (username,))
        row = cursor.fetchone()
        if row:
            user_id = row[0]
            return user_id
        else:
            return None
    except Exception as e:
        # Xử lý lỗi nếu có
        print("Lỗi khi lấy UserID:", str(e))
        return None
    finally:
        if conn:
            conn.close()
#===================================================================================================================#
# Sử dụng hàm để lấy UserID của tài khoản đang đăng nhập
current_username = get_current_username() 
user_id = get_user_id_by_username(current_username)
#=============================================================================================================
#=============================================Hàm xử lý đăng nhập và frame====================================#
def login(username, password, root):
    global current_user_info  # Khai báo biến toàn cục
    
    current_user_info = {
        "Tên đăng nhập": username,  # Sử dụng tham số username từ hàm
        "Họ và tên": "",
        "Số tài khoản": "",
        "Số dư": "",
    }

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT FullName, AccountNumber, Balance FROM Users INNER JOIN Accounts ON Users.UserID = Accounts.UserID WHERE Username=? AND Password=?", (username, password))
    user_info = cursor.fetchone()

    if user_info:
        # Lưu thông tin của tài khoản đăng nhập vào biến toàn cục
        current_user_info = {
            "Tên đăng nhập": username,        
            "Họ và tên": user_info[0],        
            "Số tài khoản": user_info[1],
            "Số dư": user_info[2],             
            
        }
        main_menu_form()
    else:
        error_label.config(text="Sai tên đăng nhập hoặc mật khẩu")
def login_frame(root):
    global error_label

    # Thay đổi kích thước hình ảnh
    image = Image.open("assets/logo/logo.png")
    image = image.resize((200, 200))

    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo, bg="#FAF1E4")
    image_label.photo = photo
    image_label.pack(side="right", padx=10, pady=10)  # Đặt hình ảnh bên phải

    # Tạo các widget và điều chỉnh giao diện người dùng
    left_frame = tk.Frame(root, bg="#FAF1E4")
    left_frame.pack(side="left", padx=10, pady=10)  # Đặt left_frame bên trái

    username_label = tk.Label(left_frame, text="Tên đăng nhập:", bg="#FAF1E4")
    username_label.pack()

    username_entry = tk.Entry(left_frame, width=40)
    username_entry.pack()

    password_label = tk.Label(left_frame, text="Mật khẩu:", bg="#FAF1E4")
    password_label.pack()

    password_entry = tk.Entry(left_frame, show="*", width=40)
    password_entry.pack()

    # Sửa lỗi ở đây, truyền tham số username_entry và password_entry cho hàm login
    login_button = tk.Button(left_frame, text="Đăng nhập", background="lightgreen", command=lambda: login(username_entry.get(), password_entry.get(), root))
    login_button.pack()

    error_label = tk.Label(left_frame, text="", fg="red")
    error_label.pack()
#=============================================================================================================
#=============================================Hàm xử chương trình chính====================================#
def main_menu_form():
    # Tạo cửa sổ tkinter cho form main_menu
    global balance_label
    main_menu_window = tk.Tk()
    main_menu_window.title("Main Menu")
    main_menu_window.geometry("600x400+200+100")
    main_menu_window.configure(bg="#FAF1E4")

    # Tạo hộp chứa thông tin tài khoản đang đăng nhập (bên trái, 1/3)
    info_frame = tk.Frame(main_menu_window, bg="#FAF1E4")
    info_frame.pack(side="left", padx=10, pady=10)

    # Hiển thị thông tin tài khoản đang đăng nhập
    row = 0  # Dòng ban đầu

    for key, value in current_user_info.items():
        label_color = "black"  # Màu chữ mặc định cho label
        field_color = "red"    # Màu chữ cho trường giá trị
        if key in ["Tên đăng nhập", "Họ và tên", "Số tài khoản", "Số dư"]:
            label_color = "black"  # Đặt màu chữ của label thành đỏ

        info_label = tk.Label(info_frame, text=f"{key}:", font=("Arial", 12), bg="#FAF1E4", fg=label_color)
        info_label.grid(row=row, column=0, sticky="w")  # Hiển thị label ở cột 0 và căn trái

        info_field = tk.Label(info_frame, text=value, font=("Arial", 12), bg="#FAF1E4", fg=field_color)
        info_field.grid(row=row, column=1, sticky="w")  # Hiển thị trường giá trị ở cột 1 và căn trái

        row += 1  # Tăng dòng cho trường tiếp theo


   # Tạo hộp chứa các nút (bên phải, 2/3)
    button_frame = tk.Frame(main_menu_window, bg="#FAF1E4")
    button_frame.pack(side="right", padx=10, pady=10)

    # Hiển thị các nút và chức năng cho form main_menu
    lblCenter = tk.Label(main_menu_window, text="VUI LÒNG CHỌN CHỨC NĂNG SỬ DỤNG", font=("Arial", 15, "bold"), fg="red", bg="#FAF1E4")
    lblCenter.place(relx=0.5, y=10, anchor="n")

    # Tạo khoảng cách giữa các nút bằng cách sử dụng pady trong pack()
    # create_account_button = tk.Button(button_frame, text="Tạo tài khoản", width=30, background="lightgreen")
    # create_account_button.pack(pady=5)

    deposit_button = tk.Button(button_frame, text="Nạp tiền vào tài khoản", width=30, background="lightgreen")
    deposit_button.pack(pady=5)

    withdraw_button = tk.Button(button_frame, text="Rút tiền từ tài khoản", width=30, background="lightgreen")
    withdraw_button.pack(pady=5)

    transfer_button = tk.Button(button_frame, text="Chuyển khoản", width=30, background="lightgreen")
    transfer_button.pack(pady=5)

    transaction_history_button = tk.Button(button_frame, text="Lịch sử giao dịch", width=30, background="lightgreen")
    transaction_history_button.pack(pady=5)

    change_password_button = tk.Button(button_frame, text="Đổi mật khẩu", width=30, background="lightgreen")
    change_password_button.pack(pady=5)

    exit_button = tk.Button(button_frame, text="Đăng xuất", width=30, background="lightgreen")
    exit_button.pack(pady=5)


    # Định nghĩa các chức năng cho các nút ở trên
    def create_account():
        # Thêm mã lệnh để mở form tạo tài khoản
        pass

    def deposit():
        username = get_current_username()  # Lấy tên đăng nhập của người đăng nhập hiện tại
        user_id = get_user_id_by_username(username) 
        show_form_deposit(user_id)

    def withdraw():
        # Thêm mã lệnh để mở form rút tiền từ tài khoản và truyền user_id
        # Thay đổi thành user_id của tài khoản đăng nhập
        username = get_current_username()  # Lấy tên đăng nhập của người đăng nhập hiện tại
        user_id = get_user_id_by_username(username)  # Lấy user_id từ tên đăng nhập

        show_form_withdrawal(user_id)


    def transfer():
        # Thêm mã lệnh để mở form chuyển khoản
        username = get_current_username()  # Lấy tên đăng nhập của người đăng nhập hiện tại
        user_id = get_user_id_by_username(username)  #
        show_transfer_form(user_id)

    def transaction_history():
        username = get_current_username()  # Lấy tên đăng nhập của người đăng nhập hiện tại
        user_id = get_user_id_by_username(username) 
        show_form_transactions(user_id)

    def change_password():
        current_username = get_current_username()
        show_change_password_form(username=current_username)



    # Khi người dùng nhấn nút, gọi các chức năng tương ứng
    #create_account_button.config(command=create_account)
    deposit_button.config(command=deposit)
    withdraw_button.config(command=withdraw)
    transfer_button.config(command=transfer)
    transaction_history_button.config(command=transaction_history)
    change_password_button.config(command=change_password)
    exit_button.config(command=exit)
    # Đặt trọng số cột để tự điều chỉnh kích thước của cột khi thay đổi kích thước cửa sổ
    main_menu_window.grid_columnconfigure(0, weight=1)
    main_menu_window.grid_columnconfigure(1, weight=2)
#=============================================================================================================
#=============================================Hàm xử lý đổi mật khẩu====================================#
def change_password(username, current_password, new_password, success_label, error_label):
    

    conn = get_db_connection()
    cursor = conn.cursor()

    # Kiểm tra thông tin đăng nhập
    cursor.execute("SELECT * FROM Users WHERE Username=? AND Password=?", (username, current_password))
    user = cursor.fetchone()

    if user:
        # Đổi mật khẩu
        cursor.execute("UPDATE Users SET Password=? WHERE Username=?", (new_password, username))
        conn.commit()
        conn.close()
        success_label.config(text="Mật khẩu đã được thay đổi thành công")
    else:
        # Đăng nhập không thành công, thông báo lỗi
        error_label.config(text="Sai tên đăng nhập hoặc mật khẩu hiện tại")
def show_change_password_form(username):
    global image_label
    # Tạo cửa sổ con (Toplevel) cho form thay đổi mật khẩu
    change_password_window = tk.Toplevel()
    change_password_window.title("Thay đổi mật khẩu")
    change_password_window.geometry("500x300+200+100")
    change_password_window.configure(bg="#FAF1E4")

    # Label trung tâm
    lblCenter = tk.Label(change_password_window, text="ĐỔI MẬT KHẨU", font=("Arial", 15, "bold"), fg="red", bg="#FAF1E4")
    lblCenter.pack()

    # Tạo hộp chứa ảnh bên phải
    image_frame = tk.Frame(change_password_window, bg="#FAF1E4")
    image_frame.pack(side="right", padx=10, pady=10)

    # Hiển thị hình ảnh
    image = Image.open("D:/PythonProject/MyBankApp/assets/logo/change_password.png")
    image = image.resize((200, 200))
    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(image_frame, image=photo, bg="#FAF1E4")
    image_label.photo = photo
    image_label.pack(side="right", padx=10, pady=10, fill="both", expand=True)

    # Tạo hộp chứa widgets bên trái
    form_frame = tk.Frame(change_password_window, bg="#FAF1E4")
    form_frame.pack(side="left", padx=10, pady=10)

    username_label = tk.Label(form_frame, text="Tên đăng nhập:", bg="#FAF1E4")
    username_label.pack()

    # Gọi hàm get_current_username và lấy giá trị trả về
    current_username = get_current_username()


    username_entry = tk.Entry(form_frame)
    username_entry.insert(0, current_username)
    username_entry.config(state="disabled")
    username_entry.pack()
    current_password_label = tk.Label(form_frame, text="Mật khẩu hiện tại:", bg="#FAF1E4")
    current_password_label.pack()

    current_password_entry = tk.Entry(form_frame, show="*")
    current_password_entry.pack()

    new_password_label = tk.Label(form_frame, text="Mật khẩu mới:", bg="#FAF1E4")
    new_password_label.pack()

    new_password_entry = tk.Entry(form_frame, show="*")
    new_password_entry.pack()

    error_label = tk.Label(form_frame, text="", fg="red")
    error_label.pack()

    success_label = tk.Label(form_frame, text="", fg="green")
    success_label.pack()

    change_password_button = tk.Button(form_frame, text="Thay đổi mật khẩu", background="lightgreen", command=lambda: change_password(username, current_password_entry.get(), new_password_entry.get(), success_label, error_label))
    change_password_button.pack()
#=============================================================================================================
#=============================================Hàm xử lý rút tiền====================================#
def execute_withdrawal_transaction(user_id, amount):
    try:
        # Lấy kết nối từ hàm get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()

        # Bắt đầu giao dịch
        conn.autocommit = False

        # Thêm giao dịch rút tiền vào bảng Transactions
        cursor.execute("INSERT INTO Transactions (TransactionType, Amount, AccountID) VALUES (?, ?, ?)", ("Withdrawal", amount, user_id))

        # Cập nhật số dư của tài khoản trong bảng Accounts
        cursor.execute("UPDATE Accounts SET Balance = Balance - ? WHERE AccountID = ?", (amount, user_id))

        # Hoàn thành giao dịch và đóng kết nối
        conn.commit()
        conn.autocommit = True
        close_connection(conn)

        return 1  # Trả về 1 nếu giao dịch thành công
    except Exception as e:
        print(str(e))
        return -1  # Trả về -1 nếu có lỗi trong quá trình giao dịch
def show_form_withdrawal(user_id):
    root = tk.Toplevel()
    root.title("Rút tiền từ tài khoản")
    lblCenter = tk.Label(root, text="RÚT TIỀN", font=("Arial", 15, "bold"), fg="red", bg="#FAF1E4")
    lblCenter.place(x=180, y=5)
    root.geometry("500x300+200+100")
    root.configure(bg="#FAF1E4")

    # Tạo frame chứa hình ảnh bên phải
    image_frame = tk.Frame(root, bg="#FAF1E4")
    image_frame.pack(side="right", padx=10, pady=10)

    # Tạo frame chứa các widget bên trái
    left_frame = tk.Frame(root, bg="#FAF1E4")
    left_frame.pack(side="left", padx=10, pady=10)

    # Hiển thị hình ảnh bên phải
    image = Image.open("D:/PythonProject/MyBankApp/assets/logo/withdraw.png")
    image = image.resize((200, 200))
    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(image_frame, image=photo, bg="#FAF1E4")
    image_label.photo = photo
    image_label.pack(side="right", padx=10, pady=10, fill="both", expand=True)

    username, balance = get_user_info(user_id)

    if username is not None and balance is not None:
        # Hiển thị thông tin người dùng bên trái
        user_info_label = tk.Label(left_frame, text=f"Tên người dùng: {username}\nSố dư tài khoản: {balance}", bg="#FAF1E4")
        user_info_label.pack()

        # Thêm các thành phần giao diện bên trái
        label = tk.Label(left_frame, text="Nhập số tiền bạn muốn rút:", bg="#FAF1E4")
        label.pack()

        # Tạo một Entry mới cho mỗi cửa sổ rút tiền và thêm vào danh sách
        amount_entry = tk.Entry(left_frame)
        amount_entry.pack()
        amount_entries.append(amount_entry)

        # Tạo một lambda function để chuyển user_id và amount_entry cho hàm handle_withdrawal
        withdrawal_button = tk.Button(left_frame, text="Rút Tiền", command=lambda: handle_withdrawal_action(user_id, amount_entry))
        withdrawal_button.pack()

    else:
        messagebox.showerror("Lỗi", "Không thể lấy thông tin người dùng.")
def handle_withdrawal_action(user_id, amount_entry):
    # Lấy số tiền từ Entry và chuyển đổi thành kiểu số thực
    amount = float(amount_entry.get())

    # Kiểm tra xem số tiền có lớn hơn 50k không
    if amount < 50000:
        messagebox.showerror("Lỗi", "Số tiền rút phải lớn hơn 50,000 VND.")
        return

    # Gọi hàm SQL để thực hiện giao dịch rút tiền
    result = execute_withdrawal_transaction(user_id, amount)

    if result == -1:
        messagebox.showerror("Lỗi", "Không thể rút tiền từ tài khoản.")
    else:
        messagebox.showinfo("Thông báo", "Giao dịch rút tiền thành công")

    # Đóng cửa sổ rút tiền sau khi hoàn thành
    root.destroy()
#=============================================================================================================
#=============================================Hàm xử lý khi nhấn vào nút nạp tiền==============================#
def show_form_deposit(user_id):
    root = tk.Toplevel()
    root.title("Nạp tiền vào tài khoản")
    lblCenter = tk.Label(root, text="NẠP TIỀN", font=("Arial", 15, "bold"), fg="red", bg="#FAF1E4")
    lblCenter.place(x=180, y=5)
    root.geometry("500x300+200+100")
    root.configure(bg="#FAF1E4")

    # Tạo frame chứa hình ảnh bên phải
    image_frame = tk.Frame(root, bg="#FAF1E4")
    image_frame.pack(side="right", padx=10, pady=10)

    # Tạo frame chứa các widget bên trái
    left_frame = tk.Frame(root, bg="#FAF1E4")
    left_frame.pack(side="left", padx=10, pady=10)

    # Hiển thị hình ảnh bên phải
    image = Image.open("D:/PythonProject/MyBankApp/assets/logo/deposit.png")
    image = image.resize((200, 200))
    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(image_frame, image=photo, bg="#FAF1E4")
    image_label.photo = photo
    image_label.pack(side="right", padx=10, pady=10, fill="both", expand=True)

    username, balance = get_user_info(user_id)

    if username is not None and balance is not None:
        # Hiển thị thông tin người dùng bên trái
        user_info_label = tk.Label(left_frame, text=f"Tên người dùng: {username}\nSố dư tài khoản: {balance}", bg="#FAF1E4")
        user_info_label.pack()

        # Thêm các thành phần giao diện bên trái
        label = tk.Label(left_frame, text="Nhập số tiền bạn muốn nạp(>50k):", bg="#FAF1E4")
        label.pack()

        # Tạo một Entry mới cho mỗi cửa sổ rút tiền và thêm vào danh sách
        amount_entry = tk.Entry(left_frame)
        amount_entry.pack()
        amount_entries.append(amount_entry)

        # Tạo một lambda function để chuyển user_id và amount_entry cho hàm handle_withdrawal
        withdraw_button = tk.Button(left_frame, text="Nạp tiền", command=lambda: handle_deposit(user_id, amount_entry))
        withdraw_button.pack()
     
    else:
        messagebox.showerror("Lỗi", "Không thể lấy thông tin người dùng.")
def handle_deposit(user_id, amount_entry):
    # Lấy số tiền từ Entry và chuyển đổi thành kiểu số thực
    amount = float(amount_entry.get())

    # Kiểm tra xem số tiền có lớn hơn 50k không
    if amount < 50000:
        messagebox.showerror("Lỗi", "Số tiền nạp phải lớn hơn 50,000 VND.")
        return

    result = execute_deposit_transaction(user_id, amount)

    if result == -1:
        messagebox.showerror("Lỗi", "Không thể nạp tiền vào tài khoản.")
    else:
        messagebox.showinfo("Thông báo", "Giao dịch nạp tiền thành công")

    # Đóng cửa sổ nạp tiền sau khi hoàn thành
    root.destroy()
def execute_deposit_transaction(user_id, amount):
    try:
        # Lấy kết nối từ hàm get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()

        # Bắt đầu giao dịch
        conn.autocommit = False

        # Thêm giao dịch nạp tiền vào bảng Transactions
        cursor.execute("INSERT INTO Transactions (TransactionType, Amount, AccountID) VALUES (?, ?, ?)", ("Deposit", amount, user_id))

        # Cập nhật số dư của tài khoản trong bảng Accounts
        cursor.execute("UPDATE Accounts SET Balance = Balance + ? WHERE AccountID = ?", (amount, user_id))

        # Hoàn thành giao dịch và đóng kết nối
        conn.commit()
        conn.autocommit = True
        close_connection(conn)

        return 1  # Trả về 1 nếu giao dịch thành công
    except Exception as e:
        print(str(e))
        return -1  # Trả về -1 nếu có lỗi trong quá trình giao dịch
#==============================================================================================================#
#=============================================Hàm xử lý khi nhấn vào nút xem giao dịch==============================#
def show_form_transactions(user_id):
    root = tk.Toplevel()
    root.title("Lịch sử giao dịch")
    lblCenter = tk.Label(root, text="LỊCH SỬ GIAO DỊCH", font=("Arial", 15, "bold"), fg="red", bg="#FAF1E4")
    lblCenter.place(x=30, y=30)
    root.geometry("800x500+200+100")
    root.configure(bg="#FAF1E4")

    # Tạo frame chứa danh sách giao dịch bên phải
    right_frame = tk.Frame(root, bg="#FAF1E4")
    right_frame.pack(side="right", padx=10, pady=30, fill="both", expand=True)

    # Tạo TreeView để hiển thị danh sách giao dịch
    tree = ttk.Treeview(right_frame, columns=("TransactionID", "TransactionType", "Amount", "TransactionDate"), show="headings")
    tree.heading("TransactionID", text="ID")
    tree.heading("TransactionType", text="Loại")
    tree.heading("Amount", text="Số tiền")
    tree.heading("TransactionDate", text="Ngày")
    tree.pack(fill="both", expand=True)
    tree.column("TransactionID", width=50)
    tree.column("TransactionType", width=150)
    tree.column("Amount", width=100)
    tree.column("TransactionDate", width=100)

    # Tạo frame chứa các widget bên trái
    left_frame = tk.Frame(root, bg="#FAF1E4")
    left_frame.pack(side="left", padx=10, pady=10)

    # Hiển thị hình ảnh bên phải (có thể thay thế bằng hình ảnh khác)
    image = Image.open("D:/PythonProject/MyBankApp/assets/logo/history_transfer.png")
    image = image.resize((200, 200))
    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(left_frame, image=photo, bg="#FAF1E4")
    image_label.photo = photo
    image_label.pack(side="right", padx=10, pady=10, fill="both", expand=True)

    # Hiển thị danh sách các giao dịch từ cơ sở dữ liệu (điều này phải được thay thế bằng dữ liệu thực tế)
    transactions = get_transactions(user_id)  # Thay thế hàm get_transactions bằng hàm thích hợp của bạn

    for transaction in transactions:
        transaction_id, transaction_type, amount, date = transaction
        # Đảm bảo kiểu dữ liệu của 'transaction_id', 'amount', và 'date' là đúng
        # Sau đó chèn giá trị vào TreeView
        tree.insert("", "end", values=(transaction_id, transaction_type, amount, date))



    # Thêm nút để đóng cửa sổ
def get_transactions(user_id):
    transactions = []
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT TransactionID, TransactionType, Amount, TransactionDate FROM Transactions "
                       "WHERE AccountID IN (SELECT AccountID FROM Accounts WHERE UserID = ?)", (user_id,))
        rows = cursor.fetchall()
        for row in rows:
            transactions.append(row)
    except Exception as e:
        print("Lỗi khi truy vấn cơ sở dữ liệu:", str(e))
    finally:
        close_connection(conn)
    return transactions
#=============================================Hàm xử lý khi nhấn vào nút chuyển tiền==============================#
def show_full_name(account_number):
    global recipient_name_var

    # Kiểm tra xem số tài khoản có tồn tại
    account_name = get_account_name_by_account_number(account_number)

    if account_name:
        # Lưu tên người nhận vào biến
        recipient_name_var.set(account_name)
    else:
        # Xóa nội dung nếu không tìm thấy tài khoản
        recipient_name_var.set("Không tìm thấy tài khoản.")
def show_transfer_form(user_id):
    global recipient_name_var
    global recipient_label
    recipient_name_var = tk.StringVar()

    # Tạo cửa sổ Toplevel cho form chuyển tiền
    transfer_window = tk.Toplevel()
    transfer_window.title("Chuyển tiền")
    transfer_window.geometry("500x300+200+100")
    transfer_window.configure(bg="#FAF1E4")

    # Tạo frame chứa thông tin nhập bên trái
    left_frame = tk.Frame(transfer_window, bg="#FAF1E4")
    left_frame.pack(side="left", padx=10, pady=10, fill="both", expand=True)

    # Label tiêu đề
    lbl_title = tk.Label(left_frame, text="Thông tin chuyển tiền", font=("Arial", 15, "bold"), fg="red", bg="#FAF1E4")
    lbl_title.pack()

    # Hiển thị thông tin về tài khoản người gửi
    sender_account_label = tk.Label(left_frame, text=f"Tài khoản người gửi: {get_full_name_by_user_id(user_id)}", bg="#FAF1E4")
    sender_account_label.pack()

    sender_balance_label = tk.Label(left_frame, text=f"Số dư: {get_account_balance(user_id)}", bg="#FAF1E4")
    sender_balance_label.pack()

    # Tạo các widget cho thông tin nhập
    # Ví dụ: Tên người nhận, số tài khoản, số tiền cần chuyển, ...
 
    account_label = tk.Label(left_frame, text="Số tài khoản:", bg="#FAF1E4")
    account_label.pack()

    account_entry = tk.Entry(left_frame)
    account_entry.pack()
    recipient_label = tk.Label(left_frame, text="Tên người nhận:", bg="#FAF1E4")
    recipient_label.pack()

    recipient_label = tk.Entry(left_frame, textvariable=recipient_name_var, state='readonly', bg="#FAF1E4")
    recipient_label.pack()


    amount_label = tk.Label(left_frame, text="Số tiền:", bg="#FAF1E4")
    amount_label.pack()

    amount_entry = tk.Entry(left_frame)
    amount_entry.pack()

    # Tạo nút để xử lý việc chuyển tiền
    transfer_button = tk.Button(left_frame, text="Chuyển tiền", background="lightgreen", command=lambda: handle_transfer(account_entry.get(), amount_entry.get()))
    transfer_button.pack()

    # Tạo frame chứa hình ảnh bên phải
    right_frame = tk.Frame(transfer_window, bg="#FAF1E4")
    right_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

    # Hiển thị hình ảnh
    image = Image.open("D:/PythonProject/MyBankApp/assets/logo/tranfer.png")  # Thay đổi đường dẫn đến hình ảnh của bạn
    image = image.resize((200, 200))
    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(right_frame, image=photo, bg="#FAF1E4")
    image_label.photo = photo
    image_label.pack(side="right", padx=10, pady=10, fill="both", expand=True)

    # Tạo Label để hiển thị tên tài khoản
    account_name_label = tk.Label(left_frame, text="", bg="#FAF1E4")
    account_name_label.pack()
   

    # Tạo nút để lấy tên tài khoản
    get_account_name_button = tk.Button(left_frame, text="Lấy Tên Tài Khoản", background="lightblue", command=lambda: show_full_name(account_entry.get()))
    get_account_name_button.pack()
def handle_transfer(sender_account_number, amount):
    try:
        amount = float(amount)
        if amount <= 0:
            messagebox.showerror("Lỗi", "Số tiền phải lớn hơn 0.")
            return

        conn = get_db_connection()

        cursor = conn.cursor()

        # Lấy ID của tài khoản người gửi
        cursor.execute("SELECT AccountID FROM Accounts WHERE AccountNumber = ?", (sender_account_number,))
        sender_account_id = cursor.fetchone()

        if sender_account_id is None:
            messagebox.showerror("Lỗi", "Không tìm thấy tài khoản người gửi.")
            return

        sender_account_id = sender_account_id[0]

        # Kiểm tra số dư tài khoản người gửi
        cursor.execute("SELECT Balance FROM Accounts WHERE AccountNumber = ?", (sender_account_number,))
        sender_balance = cursor.fetchone()

        if sender_balance is None:
            messagebox.showerror("Lỗi", "Không tìm thấy tài khoản người gửi.")
            return

        # Kiểm tra xem tài khoản người gửi có đủ tiền để chuyển hay không
        if sender_balance[0] < amount:
            messagebox.showerror("Lỗi", "Số dư trong tài khoản người gửi không đủ để chuyển số tiền này.")
            return

        # Bắt đầu giao dịch

        # Thực hiện giao dịch chuyển tiền
        cursor.execute("INSERT INTO Transactions (TransactionType, Amount, AccountID) VALUES (?, ?, ?)",
                       ("Transfer", amount, sender_account_id))

        cursor.execute("UPDATE Accounts SET Balance = Balance - ? WHERE AccountNumber = ?", (amount, sender_account_number))

        
        recipient_account_id = 1
        cursor.execute("INSERT INTO Transactions (TransactionType, Amount, AccountID) VALUES (?, ?, ?)",
                       ("Transfer", amount, recipient_account_id))

        # Hoàn thành giao dịch và đóng kết nối
        conn.commit()
        close_connection(conn)

        messagebox.showinfo("Thông báo", f"Giao dịch chuyển tiền thành công.")

    except Exception as e:
        messagebox.showerror("Lỗi", str(e))
#==============================================================================================================#
if __name__ == "__main__":
    # Tạo cửa sổ tkinter
    root = tk.Tk()
    root.title("Đăng nhập")
    root.geometry("500x280+200+100")
    root.configure(bg="#FAF1E4")
    lblCenter = tk.Label(root, text="ĐĂNG NHẬP", font=("Arial", 15, "bold"), fg="red",bg="#FAF1E4")
    lblCenter.place(x=180, y=5)
    root.resizable(False, False)
    # Hiển thị form đăng nhập
    login_frame(root)

    # Chạy ứng dụng tkinter
    root.mainloop()

