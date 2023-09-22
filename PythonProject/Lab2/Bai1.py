#Bài 1: Cài đặt lớp Sinh viên và danh sách sinh viên như sau và hoàn thành các hàm còn trống (chưa có nội dung)
from datetime import datetime
from datetime import date
# f = open("Z:\PythonProject\Lab2\sinhvien.txt", "r")
# print(f.read())

class SinhVien:
    #Biến của lớp, chung cho tất cả các đối tượng thuộc lớp
    truong = "Đại học Đà Lạt"
    # Hàm khởi tạo, hàm tạo lập: khởi gán các thuộc tính của đối tượng
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    # cho phép truy xuất tới thuộc tính từ bên ngoài thông qua trường maSO

    @property
    def maSo(self):
        return self.__maSo
    # cho phép thay đổi giá trị thuộc tính maSO
    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maSo = maso
    # Phương thức tĩnh: ccas phương thức không truy xuất gì ddeeens thuộc tính, hành vi của lớp
    # những phương thức này không cần truyền tham số mặc định self
    # đây không phải lf một hành vi( phương thức) của một đối tượng thuộc lớp
    @property
    def hoTen(self):
        return self.__hoTen

    @hoTen.setter
    def hoTen(self, hoten):
        self.__hoTen = hoten

    @property
    def ngaySinh(self):
        return self.__ngaySinh

    @ngaySinh.setter
    def ngaySinh(self, ngaySinh):
        self.__ngaySinh = ngaySinh
    @staticmethod
    def laMaSoHopLe(maso:int):
        return len(str(maso))== 7
    # Phương thức của lớp, chỉ xuất tới các biến thành viên của lớp
    #không truy cuất được các thuộc tính riêng của đối tượng
    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi
    # tương tự ghi đè phương thức toString()
    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    # hành vi của đối tượng sinh viên
    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")

class DanhSachSv:
    def __init__(self):
        self.dssv = []
    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)
    def xuat(self):
        for sv in self.dssv:
            print(sv)

    # Tìm sinh viên theo mssv, nếu có trả về sinh viên
    
    def timSvTheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.maSo == mssv]
   
    # tìm sinh viên theo msssv. nếu có trả về vị trí của sinh viên trong danh sách
  
    def timVTSvTheoMssv(self, mssv:int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:
                return i
        return -1
    # xóa sinh viên có mã số mssv, thông báo xóa được hoặc không
    
    def xoaSVTheoMssv(self, maSo:int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
    def timSvTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.hoTen.rsplit(' ', 1)[-1] == ten]
    # tim nhung sinh vien sinh truoc 15/06/2000

    def timSvSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh < ngay]


sv1 = SinhVien(2115239, "Trần Văn Nam",
               date(2003, 7, 24))
sv2 = SinhVien(2115287, "Hoàng Vũ Minh Trung",
               date(2003, 12, 5)) 
sv3 = SinhVien(2115258, "Võ Xuân Quang",
               date(2003, 11, 1)) 
sv4 = SinhVien(211817, "Trương Tấn Diệm",
               date(2003, 12, 5)) 
sv5 = SinhVien(2113014, "Phạm Anh Quân",
               date(2003, 10, 17)) 


# sv.xuat()
ds = DanhSachSv()
ds.themSinhVien(sv1)
ds.themSinhVien(sv2)
ds.themSinhVien(sv3)
ds.themSinhVien(sv4)
ds.themSinhVien(sv5)
ds.xuat()


while(True):
    msTim = int(input("Nhập vào mã số muốn tìm: "))
    kq = ds.timSvTheoMssv(msTim)
    if kq != None and len(kq) > 0:
        print("Đã tìm thấy sinh viên có mã số: ", msTim)
        for sv in kq:
            sv.xuat()
        print(ds.timVTSvTheoMssv(msTim))
        break
    else:
        print(f"Không tìm thấy sinh viên có mã {msTim}")

#  xoa sinh vien

maSo = int(input("Nhập vào mã số muốn xóa: "))
ds.xoaSVTheoMssv(maSo)
ds.xuat()

# tim ten sinh viên

# ten = input("Nhập tên muốn tìm: ")
# kq = ds.timSvTheoTen(ten)
# if kq != 0:
#     print("Đã tìm thấy sinh viên có tên:", ten)
#     for sv in kq:
#         sv.xuat()
# else:
#     print("Không tìm thấy sinh viên có tên:", ten)
while(True):
    ten = input("Nhập tên muốn tìm: ")
    kq = ds.timSvTheoTen(ten)
    if kq is not None and len(kq) > 0:
        print("Đã tìm thấy sinh viên có tên:", ten)
        for sv in kq:
            sv.xuat()
        break
    else:
        print("Không tìm thấy sinh viên có tên:", ten)


# Tim sinh viên sinh trước ngày 15/06/2000

ngay = date(2000, 6, 15)
kqNgay = ds.timSvSinhTruocNgay(ngay)
if kq != 0:
    print(f"Đã tìm thấy sinh viên sinh trước thời gian {ngay}")
    for sv in kqNgay:
        sv.xuat()
else:
    print(f"ko thấy sinh viên sinh trước thời gian {ngay}")
