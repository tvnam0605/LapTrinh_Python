day_so = [1, 5, 8, 10, 11, 15, 17, 20, 1, 7, 41]

# Hàm kiểm tra số lẻ không chia hết cho 5
def kiemTraSoLeKhongChiaHetNam(so):
    return so % 2 != 0 and so % 5 != 0

# Sử dụng hàm filter để lọc danh sách
ket_qua = list(filter(kiemTraSoLeKhongChiaHetNam, day_so))

print("Kết quả số lẻ không chia hết cho 5:", ket_qua)
# xuất các số fibonacci trong dãy
def laSofibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num

ket_qua = list(filter(laSofibonacci, day_so))
print("Các số Fibonacci trong dãy số:", ket_qua)


# Hàm kiểm tra số nguyên tố
def laSoNT(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
#sử dụng max(filter) để in ra số lớn nhất trong các số nguyên tố
ket_qua = max(filter(lambda num: laSoNT(num), day_so), default=None)
print("Số nguyên tố lớn nhất trong dãy số:", ket_qua)
# số fibonacci nhỏ nhất, sử dụng min(filter)
ket_qua = min(filter(laSofibonacci, day_so))
print("Số Fibonacci nhỏ nhất trong dãy số:", ket_qua)
#tính trung bình các số lẻ
# Hàm tính trung bình các số lẻ trong dãy số
def tinhTrungBinhSoLe(num):
    so_le = [num for num in num if num % 2 != 0]
    if len(so_le) > 0:
        trung_binh = sum(so_le) / len(so_le)
        return trung_binh
    else:
        return 0
trung_binh_so_le = tinhTrungBinhSoLe(day_so)
print("Trung bình các số lẻ trong dãy số:", trung_binh_so_le)

def tinhTichCacSoLeKhongChiaHetChoBa(numbers):
    tich = 1
    for num in numbers:
        if num % 2 != 0 and num % 3 != 0:
            tich *= num
    return tich
ket_qua = tinhTrungBinhSoLe(day_so)
print("Tích các số lẻ trong dãy số:", ket_qua)
# đổi chỗ 2 phần tử
def doiChoHaiPhanTu(danh_sach, vi_tri_1, vi_tri_2):
    if 0 <= vi_tri_1 < len(danh_sach) and 0 <= vi_tri_2 < len(danh_sach):
        danh_sach[vi_tri_1], danh_sach[vi_tri_2] = danh_sach[vi_tri_2], danh_sach[vi_tri_1]
    else:
        print("Vị trí không hợp lệ!")

# Vị trí cần đổi chỗ
vi_tri_1 = 2
vi_tri_2 = 5

doiChoHaiPhanTu(day_so, vi_tri_1, vi_tri_2)
print("Danh sách sau khi đổi chỗ:", day_so)

# đảo nược danh dách
def daoNguocDanhSach(danh_sach):
    return danh_sach[::-1]
danh_sach_dao_nguoc = daoNguocDanhSach(day_so)
print("Danh sách sau khi đảo ngược:", danh_sach_dao_nguoc)

def timSoLonThuNhi(danh_sach):
    max_1 = float('-inf')  # Số lớn nhất
    max_2 = float('-inf')  # Số lớn thứ nhì

    for num in danh_sach:
        if num > max_1:
            max_2 = max_1
            max_1 = num
        elif num > max_2 and num != max_1:
            max_2 = num

    return max_2

# Gọi hàm để tìm và in ra tất cả các số lớn thứ nhì trong danh_sach_so
so_lon_thu_nhi = timSoLonThuNhi(day_so)
print("Các số lớn thứ nhì trong danh sách:", so_lon_thu_nhi)

def tinhTongChuSo(numbers):
    tong = sum(int(chu_so) for num in numbers for chu_so in str(num))
    print("Tổng các chữ số trong danh sách:", tong)

tinhTongChuSo(day_so)
##
def demSoLanXuatHien(numbers, so_can_dem):
    dem = 0
    for num in numbers:
        if num == so_can_dem:
            dem += 1
    return dem

# Số cần đếm
so_can_dem = 5

# Gọi hàm để đếm số lần xuất hiện của so_can_dem trong danh_sach_so
so_lan_xuat_hien = demSoLanXuatHien(day_so, so_can_dem)
print(f"Số lần xuất hiện của số {so_can_dem} trong danh sách:", so_lan_xuat_hien)

#
def xuatSoXuatHienNLan(numbers, n):
    so_xuat_hien_n_lan = []
    so_lan_xuat_hien = {}
    
    for num in numbers:
        if num in so_lan_xuat_hien:
            so_lan_xuat_hien[num] += 1
        else:
            so_lan_xuat_hien[num] = 1
    
    for num, so_lan in so_lan_xuat_hien.items():
        if so_lan == n:
            so_xuat_hien_n_lan.append(num)
    
    return so_xuat_hien_n_lan

# Dãy số nguyên

# Số lần xuất hiện cần kiểm tra
n = 2
so_xuat_hien_n_lan = xuatSoXuatHienNLan(day_so, n)
print(f"Các số xuất hiện {n} lần trong danh sách:", so_xuat_hien_n_lan)

