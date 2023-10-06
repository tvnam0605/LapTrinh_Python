##Đọc và Ghi Dữ Liệu:

    pd.read_csv(): Đọc dữ liệu từ tệp CSV.
    pd.read_excel(): Đọc dữ liệu từ tệp Excel.
    pd.to_csv(): Ghi dữ liệu ra tệp CSV.
    pd.to_excel(): Ghi dữ liệu ra tệp Excel.
##Khám Phá Dữ Liệu:

    df.head(): Hiển thị các hàng đầu tiên của DataFrame.
    df.tail(): Hiển thị các hàng cuối cùng của DataFrame.
    df.info(): Hiển thị thông tin về DataFrame, bao gồm kiểu dữ liệu và số lượng giá trị không null.
    df.describe(): Tạo tóm tắt thống kê của các cột số.
##Xử Lý Dữ Liệu:

    df.head(): Hiển thị các hàng đầu tiên của DataFrame.
    df.tail(): Hiển thị các hàng cuối cùng của DataFrame.
    df.info(): Hiển thị thông tin về DataFrame, bao gồm kiểu dữ liệu và số lượng giá trị không null.
    df.describe(): Tạo tóm tắt thống kê của các cột số.
    df.drop(): Loại bỏ cột hoặc hàng từ DataFrame.
    df.fillna(): Thay thế giá trị null bằng giá trị khác.
    df.groupby(): Nhóm dữ liệu dựa trên giá trị của một hoặc nhiều cột.
    df.sort_values(): Sắp xếp DataFrame dựa trên giá trị của một hoặc nhiều cột.
    df.pivot_table(): Tạo bảng tổng hợp (pivot table).
    df.melt(): Chuyển đổi từ dạng rộng (wide) sang dạng dài (long).
##Truy xuất và Lọc Dữ Liệu:

    df['column_name']: Truy xuất một cột trong DataFrame.
    df.loc[]: Truy xuất dữ liệu theo nhãn hàng và cột.
    df.iloc[]: Truy xuất dữ liệu theo vị trí hàng và cột.
    df.query(): Truy vấn dữ liệu dựa trên điều kiện.
##Tính Toán và Thống Kê:

    df.mean(): Tính giá trị trung bình của các cột.
    df.median(): Tính giá trị trung vị của các cột.
    df.sum(): Tính tổng các cột.
    df.min(), df.max(): Tìm giá trị nhỏ nhất và lớn nhất trong các cột.
    df.std(): Tính độ lệch chuẩn của các cột.
    df.corr(): Tính ma trận tương quan giữa các cột.
##Trực Quan Hóa Dữ Liệu:

    df.plot(): Vẽ biểu đồ từ dữ liệu trong DataFrame.
##Ghép Nối Dữ Liệu:

    pd.concat(): Ghép nối (concatenate) các DataFrame theo các trục.
    pd.merge(): Ghép nối (merge) các DataFrame dựa trên cột chung.