import pyodbc
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def get_connection():
    conn = pyodbc.connect (
        "Driver={SQL Server Native Client 11.0};"
        "Server=.\SQLEXPRESS;"
        "Database=QLMonAn;"
        "Trusted Connection=yes;"
        "UID=sa;"
        "PWD=sa;"
    )
    return conn
    

def close_connection(conn):
    if conn:
        conn.close()
def load_nhom_mon_an_combobox(category_field):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Truy vấn danh sách các nhóm món ăn từ bảng NhomMonAn
        select_query = "SELECT TenNhom FROM NhomMonAn"
        cursor.execute(select_query)

        # Lấy danh sách các nhóm món ăn
        nhom_mon_an = cursor.fetchall()

        # Chuyển đổi danh sách thành chuỗi trước khi hiển thị
        nhom_mon_an_str = [str(nhom[0]) for nhom in nhom_mon_an]

        # Xóa tất cả các lựa chọn hiện tại trong Combobox
        category_field['values'] = ()

        # Thêm danh sách các nhóm món ăn đã chuyển đổi thành chuỗi vào Combobox
        category_field['values'] = nhom_mon_an_str

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi truy vấn dữ liệu. Thông tin lỗi: ", error)
def load_mon_an_treeview(treeview, selected_category=None):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        if selected_category:
            select_query = '''
                SELECT MonAn.MaMonAn, MonAn.TenMonAn, MonAn.DonViTinh, MonAn.DonGia, NhomMonAn.TenNhom 
                FROM MonAn INNER JOIN NhomMonAn ON MonAn.Nhom = NhomMonAn.MaNhom 
                WHERE NhomMonAn.TenNhom = ?'''
            cursor.execute(select_query, (selected_category,))

        else:
            select_query = '''SELECT MonAn.MaMonAn, MonAn.TenMonAn, MonAn.DonViTinh, MonAn.DonGia, NhomMonAn.TenNhom 
                                FROM MonAn INNER JOIN NhomMonAn ON MonAn.Nhom = NhomMonAn.MaNhom'''
            cursor.execute(select_query)

        # Xóa tất cả các hàng hiện tại trong treeview
        for row in treeview.get_children():
            treeview.delete(row)

        # Thêm thông tin món ăn vào treeview
        for row in cursor.fetchall():
            # Trong vòng lặp for row in cursor.fetchall():
            row = [str(item).replace("'", "") for item in row]
            treeview.insert("", "end", values=row)


        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi truy vấn dữ liệu. Thông tin lỗi: ", error)
def luu_mon_an():
    ten_mon_an = entry_mon_an.get()
    don_vi_tinh = entry_don_vi_tinh.get()
    don_gia = entry_don_gia.get()
    nhom = category_field_add.get()

    selection = mon_an_treeview.selection()
    if selection:
        sua_mon_an()
    else:
        them_mon_an()

    entry_mon_an.delete(0, 'end')
    entry_don_vi_tinh.delete(0, 'end')
    entry_don_gia.delete(0, 'end')
    category_field_add.set("")
def them_mon_an():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        ten_mon_an = entry_mon_an.get()
        don_vi_tinh = entry_don_vi_tinh.get()
        don_gia = entry_don_gia.get()
        nhom = category_field_add.get()

        # Thêm món ăn vào cơ sở dữ liệu
        insert_query = "INSERT INTO MonAn (TenMonAn, DonViTinh, DonGia, Nhom) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (ten_mon_an, don_vi_tinh, don_gia, nhom))
        connection.commit()

        load_mon_an_treeview(mon_an_treeview)

        entry_mon_an.delete(0, 'end')
        entry_don_vi_tinh.delete(0, 'end')
        entry_don_gia.delete(0, 'end')
        category_field_add.set("") 

        messagebox.showinfo("Thông báo", "Thêm món ăn thành công!")

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thêm món ăn. Thông tin lỗi: ", error)
def sua_mon_an():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Lấy thông tin từ các trường nhập liệu
        ten_mon_an = entry_mon_an.get()
        don_vi_tinh = entry_don_vi_tinh.get()
        don_gia = entry_don_gia.get()
        nhom = category_field_add.get()

        selection = mon_an_treeview.selection()
        if selection:
            selected_item = mon_an_treeview.item(selection[0])
            ma_mon_an = selected_item['values'][0]

            update_query = "UPDATE MonAn SET TenMonAn = ?, DonViTinh = ?, DonGia = ?, Nhom = ? WHERE MaMonAn = ?"
            cursor.execute(update_query, (ten_mon_an, don_vi_tinh, don_gia, nhom, ma_mon_an))

            connection.commit()

            # Làm mới cây Treeview
            load_mon_an_treeview(mon_an_treeview)

            entry_mon_an.delete(0, 'end')
            entry_don_vi_tinh.delete(0, 'end')
            entry_don_gia.delete(0, 'end')
            category_field_add.set("") 

            messagebox.showinfo("Thông báo", "Sửa món ăn thành công!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn món ăn để sửa.")

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi sửa món ăn. Thông tin lỗi: ", error)
def xoa_mon_an():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        selection = mon_an_treeview.selection()
        if selection:
            selected_item = mon_an_treeview.item(selection[0])
            ma_mon_an = selected_item['values'][0]

            # Xóa món ăn khỏi cơ sở dữ liệu
            delete_query = "DELETE FROM MonAn WHERE MaMonAn = ?"
            cursor.execute(delete_query, (ma_mon_an,))

            connection.commit()

            # Làm mới cây Treeview
            load_mon_an_treeview(mon_an_treeview)

            entry_mon_an.delete(0, 'end')
            entry_don_vi_tinh.delete(0, 'end')
            entry_don_gia.delete(0, 'end')
            category_field_add.set("") 

            messagebox.showinfo("Thông báo", "Xóa món ăn thành công!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn món ăn để xóa.")

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi xóa món ăn. Thông tin lỗi: ", error)
def chon_mon_an(event):
    selection = mon_an_treeview.selection()
    if selection:
        selected_item = mon_an_treeview.item(selection[0])
        ma_mon_an = selected_item['values'][0]
        ten_mon_an = selected_item['values'][1]
        don_vi_tinh = selected_item['values'][2]
        don_gia = selected_item['values'][3]
        nhom = selected_item['values'][4]

        entry_mon_an.delete(0, 'end')
        entry_mon_an.insert(0, ten_mon_an)
        entry_don_vi_tinh.delete(0, 'end')
        entry_don_vi_tinh.insert(0, don_vi_tinh)
        entry_don_gia.delete(0, 'end')
        entry_don_gia.insert(0, don_gia)
        category_field_add.set(nhom)
def on_combobox_select(event):
    selected_category = category_field.get()
    load_mon_an_treeview(mon_an_treeview, selected_category)
if __name__ == "__main__":
    root = Tk()

    root.title("Quản lý món ăn")
    root.geometry("600x500+250+100")
    root.resizable(True, False)

    Label(root, text="Nhóm món ăn", font=("Arial", 11, "bold")).place(x=30, y=10)

    category_field = ttk.Combobox(root, width=35)
    category_field.place(x=350, y=10)
    load_nhom_mon_an_combobox(category_field)

    # Tạo treeview để hiển thị thông tin món ăn
    columns = ("Mã Món Ăn", "Tên Món Ăn", "Đơn Vị Tính", "Đơn Giá", "Nhóm")
    mon_an_treeview = ttk.Treeview(root, columns=columns, show='headings')
    mon_an_treeview.heading("Mã Món Ăn", text="Mã Món Ăn")
    mon_an_treeview.heading("Tên Món Ăn", text="Tên Món Ăn")
    mon_an_treeview.heading("Đơn Vị Tính", text="Đơn Vị Tính")
    mon_an_treeview.heading("Đơn Giá", text="Đơn Giá")
    mon_an_treeview.heading("Nhóm", text="Nhóm")

    mon_an_treeview.column("Mã Món Ăn", width=100)
    mon_an_treeview.column("Tên Món Ăn", width=200)
    mon_an_treeview.column("Đơn Vị Tính", width=100)
    mon_an_treeview.column("Đơn Giá", width=80)
    mon_an_treeview.column("Nhóm", width=90)

    mon_an_treeview.place(x=10, y=50)

    load_mon_an_treeview(mon_an_treeview)

    # Tạo các trường nhập liệu cho thông tin món ăn
    label_mon_an = Label(root, text="Tên Món Ăn")
    label_mon_an.place(x=10, y=290)
    entry_mon_an = Entry(root)
    entry_mon_an.place(x=150, y=290)

    label_don_vi_tinh = Label(root, text="Đơn Vị Tính")
    label_don_vi_tinh.place(x=10, y=320)
    entry_don_vi_tinh = Entry(root)
    entry_don_vi_tinh.place(x=150, y=320)

    label_don_gia = Label(root, text="Đơn Giá")
    label_don_gia.place(x=10, y=350)
    entry_don_gia = Entry(root)
    entry_don_gia.place(x=150, y=350)

    # Tạo Combobox để chọn nhóm cho món ăn
    label_nhom = Label(root, text="Nhóm")
    label_nhom.place(x=10, y=380)
    category_field_add = ttk.Combobox(root, width=35)
    category_field_add.place(x=150, y=380)
    load_nhom_mon_an_combobox(category_field_add)
    # Bổ sung nút lưu khi thêm hoặc sửa món ăn
    btn_save = Button(root, text="Lưu",fg="Blue", command=luu_mon_an)
    btn_save.place(x=430, y=410)

    # Tạo nút thêm món ăn
    btn_add = Button(root, text="Thêm Món Ăn",fg="Blue", command=them_mon_an)
    btn_add.place(x=10, y=410)

    # Tạo nút sửa món ăn
    btn_edit = Button(root, text="Sửa Món Ăn",fg="Blue", command=sua_mon_an)
    btn_edit.place(x=150, y=410)
    mon_an_treeview.bind("<ButtonRelease-1>", chon_mon_an)
    category_field.bind("<<ComboboxSelected>>", on_combobox_select)
    # Tạo nút xóa món ăn
    btn_delete = Button(root, text="Xóa Món Ăn",fg="Red", command=xoa_mon_an)
    btn_delete.place(x=290, y=410)
    btn_delete = Button(root, text="Thoát",fg="Red", command=exit)
    btn_delete.place(x=530, y=410)

    root.mainloop()
