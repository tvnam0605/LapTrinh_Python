import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\PythonProject\Lab6\sales_data.csv")
print(df)
##Trả lời câu hỏi
'''Sử dụng pandas đọc tập tin dữ liệu sales_data.csv và thực hiện các yêu cầu sau:
1) Hiển thị thông tin của dữ liệu, xem và trả lời các câu hỏi sau:

• Dữ liệu này có bao nhiêu cột, tên của các cột là gì?
- dữ liệu có 9 cột, tên của các cột là 
            month_number  
            facecream  
            facewash  
            toothpaste  
            bathingsoap  
            shampoo  
            moisturizer  
            total_units  
            total_profit
• Kiểu dữ liệu của các cột
sử dụng # data_types = df.dtypes

# # In ra kết quả
# print(data_types)

            month_number    int64
            facecream       int64
            facewash        int64
            toothpaste      int64
            bathingsoap     int64
            shampoo         int64
            moisturizer     int64
            total_units     int64
            total_profit    int64
• Có bao nhiêu cột có chứa giá trị null
khong có cột nào chứa giá trị null
# Kiểm tra xem từng cột có chứa giá trị null không
columns_with_null = df.isnull().sum()

# In ra kết quả
print(columns_with_null)
            month_number    0
            facecream       0
            facewash        0
            toothpaste      0
            bathingsoap     0
            shampoo         0
            moisturizer     0
            total_units     0
            total_profit    0
2) Hiển thị nội dung toàn bộ dữ liệu'''
print(df)

# data_types = df.dtypes

# # In ra kết quả
# print(data_types)

# Kiểm tra xem từng cột có chứa giá trị null không
columns_with_null = df.isnull().sum()

# In ra kết quả
print(columns_with_null)

# 3) Xuất hàng dữ liệu của tháng có lợi nhuận cao nhất như sau:
max_profit_month = df[df['total_profit'] == df['total_profit'].max()]
print("tháng có lợi nhuận cao nhất:")
print(max_profit_month)

# 4) Xuất hàng dữ liệu của tháng bán nhiều mặt hàng nhất
max_units_month = df[df['total_units'] == df['total_units'].max()]
print("tháng bán nhiều mặt hàng nhất:")
print(max_units_month)

# 5) Xuất hàng dữ liệu của tháng bán nhiều kem đánh răng nhất
max_toothpaste_month = df[df['toothpaste'] == df['toothpaste'].max()]
print("Tháng bán nhiều kem đánh răng nhất:")
print(max_toothpaste_month)

# 6) Cho biết tổng lợi nhuận của cả năm
total_yearly_profit = df['total_profit'].sum()
print("Tổng lợi nhuận của cả năm:", total_yearly_profit)

# 7) Cho biết tổng số lượng đã bán theo mặt hàng
total_units_by_product = df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()
print("Tổng số lượng đã bán theo mặt hàng:")
print(total_units_by_product)

# 8) Hiển thị số lượng các mặt hàng bán trong tháng 2
product_sales_february = df[df['month_number'] == 2][['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']]
print("Số lượng các mặt hàng bán trong tháng 2:")
print(product_sales_february)

# 9) Số lượng mặt hàng bán chạy nhất tháng 2 (6100)
product_sold_most_february = product_sales_february.max().idxmax()
quantity_sold_most_february = product_sales_february.max().max()
print(f"Mặt hàng bán chạy nhất trong tháng 2: {product_sold_most_february} ({quantity_sold_most_february} đơn vị)")

# 10) Tìm mặt hàng bán chạy nhất trong năm (bathingsoap)
total_units_by_product_year = df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()
most_sold_product_year = total_units_by_product_year.idxmax()
quantity_sold_most_year = total_units_by_product_year.max()
print(f"Mặt hàng bán chạy nhất trong năm: {most_sold_product_year} ({quantity_sold_most_year} đơn vị)")