from Bai3 import PhanSo

class MangPhanSo:
    def __init__(self, ds: list = None) -> None:
        if ds is not None:
            self.ds = ds
        else:
            self.ds = []

    def them(self, ps):
        self.ds.append(ps)

    def xuat(self):
        for ps in self.ds:
            print(ps)

    def docTuFile(self, fileName):
        with open(fileName, 'r', encoding='utf-8') as f:
            for hang in f:
                du_lieu = hang.split('/')
                self.them(PhanSo(int(du_lieu[0]), int(du_lieu[1])))

    def DemAm(self):
        Dem = 0
        for ps in self.ds:
            if ps.tu < 0 or ps.mau < 0:  # Sửa điều kiện này
                Dem += 1
        return Dem

    def tongPSAm(self):
        Tong = 0
        for ps in self.ds:
            if ps.tu < 0 or ps.mau < 0:
                Tong += ps.tu // ps.mau  # Sử dụng // để thực hiện phép chia nguyên
        return Tong

    def timPhanSoDuongMin(self):
        phan_so_duong_min = None
        for ps in self.ds:
            if ps.tu > 0 and ps.mau > 0:
                if phan_so_duong_min is None:
                    phan_so_duong_min = ps
                elif ps.tu / ps.mau < phan_so_duong_min.tu / phan_so_duong_min.mau:
                    phan_so_duong_min = ps
        return phan_so_duong_min

    def timPhanSoAm(self):
        return MangPhanSo([ps for ps in self.ds if ps.tu < 0 or ps.mau < 0])

    def xoaPhanSoX(self, x):
        if x in self.ds:
            self.ds.remove(x)

    def xoaPhanSo(self, x: PhanSo):
        self.ds = [ps for ps in self.ds if ps != x]

    def xoaPhanSoTuLaX(self, x):
        self.ds = [ps for ps in self.ds if ps.tu != x]

    def timViTriPhanSo(self, x):  # Thêm self ở đây
        vi_tri = []
        for i, phan_so in enumerate(self.ds):
            if phan_so == x:
                vi_tri.append(i)
        return vi_tri

# Sử dụng ví dụ tạo một đối tượng MangPhanSo và đọc dữ liệu từ tệp du_lieu.txt
mang_phan_so = MangPhanSo()
mang_phan_so.docTuFile("D:/PythonProject/Lab2/du_lieu.txt")

print("Danh sách phân số:")
mang_phan_so.xuat()

so_luong_am = mang_phan_so.DemAm()
print(f"Số lượng phân số âm trong mảng: {so_luong_am}")

danh_sach_phan_so_am = mang_phan_so.timPhanSoAm()
print("Danh sách phân số âm trong mảng: ")
for ps in danh_sach_phan_so_am.ds:  # Truy cập thuộc tính ds
    print(str(ps))

phan_so_be_nhat = mang_phan_so.timPhanSoDuongMin()
print(f"Phân số nhỏ nhất trong mảng là: {str(phan_so_be_nhat)}")

tong_phan_so_am = mang_phan_so.tongPSAm()
print(f"Tổng phân số âm trong mảng là: {tong_phan_so_am}")

print("Danh sách phân số trước khi xóa:")
mang_phan_so.xuat()

# Xóa phân số PhanSo(1, 10) khỏi danh sách
phanso_xoa = PhanSo(1, 10)
mang_phan_so.xoaPhanSo(phanso_xoa)

print("Danh sách phân số sau khi xóa:")
mang_phan_so.xuat()

# Tạo một phân số để tìm vị trí
phanso_tim = PhanSo(1, 10)

# Tìm tất cả vị trí của phân số trong mảng
vi_tri = mang_phan_so.timViTriPhanSo(phanso_tim)  # Gọi phương thức timViTriPhanSo

if vi_tri:
    print(f"Phân số {str(phanso_tim)} được tìm thấy tại các vị trí: {vi_tri}")
else:
    print(f"Phân số {str(phanso_tim)} không có trong mảng.")

# Xóa phân số có tử là x
x = 4
mang_phan_so.xoaPhanSoTuLaX(x)

# In danh sách sau khi xóa
print(f"Danh sách sau khi xóa phân số có tử là {x}:")
mang_phan_so.xuat()

# Sắp xếp tăng dần
mang_phan_so.ds.sort()
print("Danh sách sau khi sắp xếp tăng dần:")
mang_phan_so.xuat()

# Sắp xếp giảm dần
mang_phan_so.ds.sort(reverse=True)
print("Danh sách sau khi sắp xếp giảm dần:")
mang_phan_so.xuat()
