class HangHoa:
    def __init__(self, ma="", ten="", nsx="", g=0.0):
        self.maHang = ma
        self.tenHang = ten
        self.nhaSX = nsx
        self.gia = g
    
    def inp(self):
        self.maHang = input("Nhap ma hang: ")
        self.tenHang = input("Nhap ten hang: ")
        self.nhaSX = input("Nhap nha san xuat: ")
        self.gia = float(input("Nhap gia: "))
    
    def out(self):
        print(f"Ma hang: {self.maHang}")
        print(f"Ten hang: {self.tenHang}")
        print(f"Nha san xuat: {self.nhaSX}")
        print(f"Gia: {self.gia:.2f}")


class HangDienMay(HangHoa):
    def __init__(self, ma="", ten="", nsx="", g=0.0, tg=0, cs=0.0, dien=0.0):
        super().__init__(ma, ten, nsx, g)
        self.tgianBH = tg
        self.congsuat = cs
        self.dienap = dien
    
    def inp(self):
        super().inp()
        self.tgianBH = int(input("Nhap thoi gian bao hanh: "))
        self.congsuat = float(input("Nhap cong suat: "))
        self.dienap = float(input("Nhap dien ap: "))
    
    def out(self):
        super().out()
        print(f"Thoi gian bao hanh: {self.tgianBH} thang")
        print(f"Cong suat: {self.congsuat} W")
        print(f"Dien ap: {self.dienap} V")


class HangSanhSu(HangHoa):
    def __init__(self, ma="", ten="", nsx="", g=0.0, cl=""):
        super().__init__(ma, ten, nsx, g)
        self.chatlieu = cl
    
    def inp(self):
        super().inp()
        self.chatlieu = input("Nhap chat lieu: ")
    
    def out(self):
        super().out()
        print(f"Chat lieu: {self.chatlieu}")


class HangThucPham(HangHoa):
    def __init__(self, ma="", ten="", nsx="", g=0.0, date="", nhh=""):
        super().__init__(ma, ten, nsx, g)
        self.ngaySX = date
        self.ngayHH = nhh
    
    def inp(self):
        super().inp()
        self.ngaySX = input("Nhap ngay san xuat (dd/mm/yyyy): ")
        self.ngayHH = input("Nhap ngay het han (dd/mm/yyyy): ")
    
    def out(self):
        super().out()
        print(f"Ngay san xuat: {self.ngaySX}")
        print(f"Ngay het han: {self.ngayHH}")


if __name__ == "__main__":
    dm = HangDienMay()
    print("Nhap thong tin hang dien may:")
    dm.inp()
    print("\nThong tin hang dien may:")
    dm.out()
    
    ss = HangSanhSu()
    print("\nNhap thong tin hang sanh su:")
    ss.inp()
    print("\nThong tin hang sanh su:")
    ss.out()
    
    tp = HangThucPham()
    print("\nNhap thong tin hang thuc pham:")
    tp.inp()
    print("\nThong tin hang thuc pham:")
    tp.out()