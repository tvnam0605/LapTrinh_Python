from datetime import datetime

class Sach:
    def __init__(self, ten_sach: str, ten_tg: str, ngay_xb: datetime, so_trang: int, gia_ban: int):
        self.ten_sach = ten_sach
        self.ten_tg = ten_tg
        self.ngay_xb = ngay_xb
        self.so_trang = so_trang
        self.gia_ban = gia_ban

    def __str__(self) -> str:
        return f"{self.ten_sach}\t{self.ten_tg} \t {self.ngay_xb} \t {self.so_trang} \t {self.gia_ban}"

    def xuat(self):
        print(f"{self.ten_sach}\t{self.ten_tg} \t {self.ngay_xb} \t {self.so_trang} \t {self.gia_ban}")


class DsSach:
    def __init__(self, ds: list = None) -> None:
        self.ds = ds if ds is not None else []

    def them(self, sa: Sach):
        self.ds.append(sa)

    def xuat(self):
        for sach in self.ds:
            print(sach)


    def timTheoTG(self, ten_tg):
        return DsSach([sach for sach in self.ds if sach.ten_tg == ten_tg])

    def timTheoNamXb(self, nam_xb):
        return DsSach([sach for sach in self.ds if sach.ngay_xb.year == nam_xb])

    def timTheoSoTrang(self, so_trang):
        return DsSach([sach for sach in self.ds if sach.so_trang == so_trang])

    def sapXepTheoTenTG(self):
        self.ds.sort(key=lambda sach: sach.ten_tg)

    def sapXepTheoNamXb(self):
        self.ds.sort(key=lambda sach: sach.ngay_xb)

    def docTuFile(self, fileName):
        with open(fileName, 'r', encoding='utf-8') as f:
            for hang in f:
                du_lieu = hang.strip().split('\t')
                if len(du_lieu) == 5:
                    ten_sach, ten_tg, ngay_xb_str, so_trang_str, gia_ban_str = du_lieu
                    try:
                        ngay_xb = datetime.strptime(ngay_xb_str, '%Y-%m-%d')
                        so_trang = int(so_trang_str)
                        gia_ban = int(gia_ban_str)
                        sach = Sach(ten_sach, ten_tg, ngay_xb, so_trang, gia_ban)
                        self.them(sach)
                    except ValueError:
                        print(hang)
                else:
                    print(hang)


if __name__ == "__main__":
    print("Danh sách sách :")
    ds_sach = DsSach()
    ds_sach.docTuFile("D:\PythonProject\Lab2\sach.txt")

   
    
    ds_sach.xuat()


    # # In danh sách sách chưa sắp xếp
    # print("Danh sách sách chưa sắp xếp:")
    # ds_sach = DsSach()
    # # Sử dụng các phương thức tìm kiếm và sắp xếp
    # ds_theo_tg = ds_sach.timTheoTG("Tác giả 1")
    # ds_theo_nam_xb = ds_sach.timTheoNamXb(2022)
    # ds_theo_so_trang = ds_sach.timTheoSoTrang(300)

    # # In danh sách sách theo các tiêu chí tìm kiếm
    # print("Danh sách sách theo tác giả:")
    # ds_theo_tg.xuat()

    # print("\nDanh sách sách xuất bản năm 2022:")
    # ds_theo_nam_xb.xuat()

    # print("\nDanh sách sách có 300 trang:")
    # ds_theo_so_trang.xuat()

    # # Sắp xếp danh sách sách
    # ds_sach.sapXepTheoTenTG()
    # print("\nDanh sách sách sau khi sắp xếp theo tên tác giả:")
    # ds_sach.xuat()

    # ds_sach.sapXepTheoNamXb()
    # print("\nDanh sách sách sau khi sắp xếp theo năm xuất bản:")
    # ds_sach.xuat()
