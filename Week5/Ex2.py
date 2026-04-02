class TtinChung:
    def __init__(self, ma="", ten="", ns=0, dc="", hsl=0, ltd=0):
        self.maNV = ma
        self.tenNV = ten
        self.namsinh = ns
        self.diachi = dc
        self.hesoluong = hsl
        self.luongtoida = ltd
    
    def inp(self):
        self.maNV = input("Nhap ma nhan vien: ")
        self.tenNV = input("Nhap ten nhan vien: ")
        self.namsinh = int(input("Nhap nam sinh: "))
        self.diachi = input("Nhap dia chi: ")
        self.hesoluong = float(input("Nhap he so luong (>0): "))
        self.luongtoida = float(input("Nhap luong toi da: "))
    
    def out(self):
        print(f"Ma nhan vien: {self.maNV}")
        print(f"Ten nhan vien: {self.tenNV}")
        print(f"Nam sinh: {self.namsinh}")
        print(f"Dia chi: {self.diachi}")
        print(f"He so luong: {self.hesoluong}")
        print(f"Luong toi da: {self.luongtoida}")
    
    def tinhluong(self):
        return self.hesoluong * self.luongtoida
    
    def tangluong(self, delta):
        hsmoi = self.hesoluong + delta
        luongmoi = hsmoi * self.luongtoida
        if luongmoi > self.luongtoida:
            print(f"Khong the tang luong! Luong moi vuot luong toi da ({self.luongtoida:.0f}).")
        self.hesoluong = hsmoi
        return luongmoi <= self.luongtoida


class CongtacVien(TtinChung):
    def __init__(self, ma="", ten="", ns=0, dc="", hsl=0, ltd=0, thhd=0, pc=0):
        super().__init__(ma, ten, ns, dc, hsl, ltd)
        self.thoihanhopdong = thhd
        self.phucap = pc
    
    def inp(self):
        super().inp()
        self.thoihanhopdong = int(input("Nhap thoi han hop dong (thang): "))
        self.phucap = float(input("Nhap phu cap: "))
    
    def out(self):
        super().out()
        print(f"Thoi han hop dong: {self.thoihanhopdong} thang")
        print(f"Phu cap: {self.phucap}")


class NhanvienChthuc(TtinChung):
    def __init__(self, ma="", ten="", ns=0, dc="", hsl=0, ltd=0, vt=""):
        super().__init__(ma, ten, ns, dc, hsl, ltd)
        self.vitri = vt
    
    def inp(self):
        super().inp()
        self.vitri = input("Nhap vi tri: ")
    
    def out(self):
        super().out()
        print(f"Vi tri: {self.vitri}")


class Truongphong(TtinChung):
    def __init__(self, ma="", ten="", ns=0, dc="", hsl=0, ltd=0, nql="", pcql=0):
        super().__init__(ma, ten, ns, dc, hsl, ltd)
        self.ngayqly = nql
        self.phucapqly = pcql
    
    def inp(self):
        super().inp()
        self.ngayqly = input("Nhap ngay quan ly (dd/mm/yyyy): ")
        self.phucapqly = float(input("Nhap phu cap quan ly: "))
    
    def out(self):
        super().out()
        print(f"Ngay quan ly: {self.ngayqly}")
        print(f"Phu cap quan ly: {self.phucapqly}")


if __name__ == "__main__":
    n = int(input("Nhap so luong can bo: "))
    ds = []
    
    for i in range(n):
        print(f"Nhap thong tin can bo thu {i + 1}:")
        loai = int(input("Chon loai can bo (1 - Cong tac vien, 2 - Nhan vien chinh thuc, 3 - Truong phong): "))
        
        cb = None
        if loai == 1:
            cb = CongtacVien()
        elif loai == 2:
            cb = NhanvienChthuc()
        elif loai == 3:
            cb = Truongphong()
        else:
            print("Loai can bo khong hop le. Bo qua.")
            continue
        
        cb.inp()
        ds.append(cb)
    
    print("\n=== THONG TIN CAN BO ===")
    for cb in ds:
        cb.out()
        print(f"Luong: {cb.tinhluong()}")
        print("Tang luong 0.5 he so luong...")
        cb.tangluong(0.5)
        print(f"Luong sau khi tang: {cb.tinhluong()}\n")