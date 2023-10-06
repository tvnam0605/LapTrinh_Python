import pandas as pd
df = pd.read_csv("D:\PythonProject\Lab6\Automobile_data.csv")

print(df)

# xuat 6 dong dau tien
#print(df.head(6))

# xuat 7 don cuoi dung

#print(df.tail(7))

# xuat ra man hinh ten cong ti co xe o to dat nhat
# df = df [['company','price']][df.price==df['price'].max()]
# print(df)
# xuat thog tin chi tiet cua tat ca cac xe thuoc hang toyota
# car_Manufactures = df.groupby('company')
# toyoyaDf = car_Manufactures.get_group("toyota")
# print(toyoyaDf)

#Đếm số xe của từng hãng
# count_car = df['company'].value_counts()
# print(count_car)
#Hãy hiển thị giá xe cao nhất của mỗi hãng xe như sau
max_price_by_company = df.groupby('company')['price'].max().reset_index()

# In ra kết quả
print(max_price_by_company)
#Hiển thị giá xe trung bình của mỗi hãng xe
# Sử dụng hàm groupby để nhóm dữ liệu theo cột 'company', sau đó tính giá xe trung bình trong mỗi hãng
average_price_by_company = df.groupby('company')['price'].mean().reset_index()

# In ra kết quả
print(average_price_by_company)