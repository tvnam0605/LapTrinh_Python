import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\PythonProject\Lab6\sales_data.csv")
print(df.info())


# profitList = df ['total_profit'].tolist()
# monthList = df ['month_number'].tolist()

# plt.figure("Biểu đồ đoạn thẳng")
# plt.plot(monthList, profitList)
# plt.xlabel('Tháng')
# plt.ylabel('Lợi nhuận ($)')
# plt.xticks(monthList)
# plt.title('Lợi nhuận hàng tháng năm 2021')
# plt.yticks([100000, 200000, 300000, 400000, 500000])
# plt.show()
# #2) Chỉnh sửa biểu đồ ở câu trên thành dạng sau:
# profitList = df ['total_profit'].tolist()
# monthList = df ['month_number'].tolist()

# plt.figure("Biểu đồ đoạn thẳng")
# plt.plot(monthList, profitList, marker='o', linestyle = '--', color='green', linewidth=2, markersize=6)
# plt.xlabel('Tháng')
# plt.ylabel('Lợi nhuận ($)')
# plt.xticks(monthList)
# plt.title('Lợi nhuận hàng tháng năm 2021')
# plt.yticks([100000, 200000, 300000, 400000, 500000])
# plt.grid(True)  # Hiển thị lưới
# plt.show()
# #Nhìn vào biểu đồ, cho biết tháng có lợi nhuận cao nhất: tháng 11
# ##3) Vẽ biểu đồ đường thể hiện số lượng bán của từng mặt hàng trong năm như sau:
# # Tạo biểu đồ cột cho số lượng bán của từng mặt hàng trong năm
# # Tạo biểu đồ đường cho số lượng bán của từng mặt hàng trong năm
# plt.figure(figsize=(10, 6))
# plt.plot(df['month_number'], df['facecream'], label='Face Cream', marker='o', color='blue', linewidth=2)
# plt.plot(df['month_number'], df['facewash'], label='Face Wash', marker='o', color='orange', linewidth=2)
# plt.plot(df['month_number'], df['toothpaste'], label='Toothpaste', marker='o', color='green', linewidth=2)
# plt.plot(df['month_number'], df['bathingsoap'], label='BathingSoap', marker='o', color='red', linewidth=2)
# plt.plot(df['month_number'], df['shampoo'], label='Shampoo', marker='o', color='violet', linewidth=2)
# plt.plot(df['month_number'], df['moisturizer'], label='Moisturizer', marker='o', color='brown', linewidth=2)

# plt.xlabel('Tháng')
# plt.ylabel('Số lượng bán')
# plt.title('Số lượng bán của từng mặt hàng trong năm')
# plt.xticks(df['month_number'])
# plt.legend()
# plt.grid(True)
# plt.show()

# #) Hiển thị số lượng bán của mặt hàng sữa rửa mặt và kem dưỡng da mặt theo tháng
# #bằng biểu đồ Điểm (biểu đồ tán xạ)
# df_facewash = df[['month_number', 'facewash']]
# df_moisturizer = df[['month_number', 'moisturizer']]
# plt.scatter(df_facewash['month_number'], df_facewash['facewash'], label='Sữa rửa mặt', color='blue', marker='o')
# plt.scatter(df_moisturizer['month_number'], df_moisturizer['moisturizer'], label='Kem dưỡng da mặt', color='green', marker='o')

# plt.xlabel('Tháng')
# plt.ylabel('Số lượng bán')
# plt.title('Số lượng bán của sữa rửa mặt và kem dưỡng da mặt theo tháng')
# plt.xticks(df['month_number'])
# plt.legend()
# plt.show()
# #5) Vẽ biểu đồ cột thể hiện số lượng xà bông tắm đã bán
# # Lọc dữ liệu cho mặt hàng "xà bông tắm"
# df_bathingsoap = df[['month_number', 'bathingsoap']]

# # Vẽ biểu đồ cột cho số lượng xà bông tắm đã bán theo tháng
# plt.figure(figsize=(10, 6))
# plt.bar(df_bathingsoap['month_number'], df_bathingsoap['bathingsoap'], label='Xà bông tắm', color='red')
# plt.xlabel('Tháng')
# plt.ylabel('Số lượng bán')
# plt.title('Số lượng xà bông tắm đã bán theo tháng')
# plt.xticks(df_bathingsoap['month_number'])
# plt.legend()
# plt.grid(True)
# plt.show()
# # Hiển thị số lượng bán của mặt hàng sữa rửa mặt và kem dưỡng da mặt theo tháng
# # bằng biểu đồ cột
# # Lọc dữ liệu cho mặt hàng "sữa rửa mặt" và "kem dưỡng da mặt"
# df_facewash = df[['month_number', 'facewash']]
# df_facecream = df[['month_number', 'facecream']]

# # Vẽ biểu đồ cột cho số lượng bán của từng mặt hàng
# plt.figure(figsize=(10, 6))
# plt.bar(df_facecream['month_number'], df_facecream['facecream'], label='Kem dưỡng da mặt', color='green', width=0.4)
# plt.bar(df_facewash['month_number'] + 0.4, df_facewash['facewash'], label='Sữa rửa mặt', color='red', width=0.4)

# plt.xlabel('Tháng')
# plt.ylabel('Số lượng bán')
# plt.title('Số lượng bán của mặt hàng "Sữa rửa mặt" và "Kem dưỡng da mặt" theo tháng')
# plt.xticks(df_facewash['month_number'])
# plt.legend()
# plt.grid(True)
# plt.show()

# # # Tính tổng số lượng bán của từng sản phẩm trong năm
# total_units = df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()

# # Tạo danh sách sản phẩm và tỉ lệ tương ứng
# products = total_units.index
# sales = total_units.values

# # Vẽ biểu đồ tròn
# plt.figure(figsize=(8, 8))
# plt.pie(sales, labels=products, autopct='%1.1f%%', startangle=140)
# plt.title('Tỉ lệ sản phẩm bán trong năm')
# plt.show()

# #Vẽ biểu đồ tròn thể hiện tỉ lệ sản phẩm bán trong tháng 3/2021
# df_march = df[df['month_number'] == 3]

# # Tính tổng số lượng bán của từng sản phẩm trong tháng
# total_units = df_march[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()

# # Tạo danh sách sản phẩm và tỉ lệ tương ứng
# products = total_units.index
# sales = total_units.values

# # Vẽ biểu đồ tròn
# plt.figure(figsize=(8, 8))
# plt.pie(sales, labels=products, autopct='%1.1f%%', startangle=140)
# plt.title('Tỉ lệ sản phẩm bán trong tháng 3')
# plt.show()

'''9) Vẽ dạng 2 hay nhiều biểu đồ con như sau:'''
# Tạo một hình và hai trục (ax1 và ax2)
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6))

ax1.plot(df['month_number'], df['bathingsoap'], label='Bathing Soap',marker='o', color='green')
ax1.set_xlabel('Tháng')
ax1.set_ylabel('Số lượng')
ax1.set_title('Số lượng xà bông tắm đã bán',color='green')
ax1.legend()

# Vẽ biểu đồ cột trên ax2
ax2.plot(df['month_number'], df['facewash'], label='Face wash',marker='o', color='red')
ax2.set_xlabel('Tháng')
ax2.set_ylabel('Số lượng')
ax2.set_title('Số lượng sữa rửa mặt đã bán',color='red')
ax2.legend()

# df_march = df[df['month_number'] == 3]
# total_units = df_march[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()
# products = total_units.index
# sales = total_units.values
# ax3.pie(sales, labels=products, autopct='%1.1f%%', startangle=140)
# ax3.set_title('Tỉ lệ sản phẩm bán trong tháng 3')


plt.tight_layout()
plt.show()