class Canbo:
    def __init__(self, ht="", t=0, gt="", dc=""):
        self.hoten = ht
        self.tuoi = t
        self.gioitinh = gt
        self.diachi = dc
    
    def inp(self):
        self.hoten = input("Nhap ho ten: ")
        self.tuoi = int(input("Nhap tuoi: "))
        self.gioitinh = input("Nhap gioi tinh (Nam / Nu / Khac): ")
        self.diachi = input("Nhap dia chi: ")
    
    def out(self):
        print(f"Ho ten: {self.hoten}")
        print(f"Tuoi: {self.tuoi}")
        print(f"Gioi tinh: {self.gioitinh}")
        print(f"Dia chi: {self.diachi}")
    
    def getTen(self):
        return self.hoten


class Congnhan(Canbo):
    def __init__(self, ht="", t=0, gt="", dc="", b=0):
        super().__init__(ht, t, gt, dc)
        self.bac = b
    
    def inp(self):
        super().inp()
        self.bac = int(input("Nhap bac: "))
    
    def out(self):
        super().out()
        print(f"Bac: {self.bac}")


class Kysu(Canbo):
    def __init__(self, ht="", t=0, gt="", dc="", ndt=""):
        super().__init__(ht, t, gt, dc)
        self.nganh = ndt
    
    def inp(self):
        super().inp()
        self.nganh = input("Nhap nganh dao tao: ")
    
    def out(self):
        super().out()
        print(f"Nganh dao tao: {self.nganh}")


class Nhanvien(Canbo):
    def __init__(self, ht="", t=0, gt="", dc="", cv=""):
        super().__init__(ht, t, gt, dc)
        self.congviec = cv
    
    def inp(self):
        super().inp()
        self.congviec = input("Nhap cong viec: ")
    
    def out(self):
        super().out()
        print(f"Cong viec: {self.congviec}")


class QLCB:
    def __init__(self):
        self.ds = []
    
    def themcb(self, cb):
        self.ds.append(cb)
    
    def timcb(self, ten):
        for cb in self.ds:
            if cb.getTen() == ten:
                cb.out()
                return
        print(f"Khong tim thay can bo co ten {ten}")
    
    def hiencb(self):
        for cb in self.ds:
            cb.out()
    
    def thoat(self):
        self.ds.clear()


def menu():
    print("1. Them can bo")
    print("2. Tim kiem can bo theo ten")
    print("3. Hien thi thong tin ve danh sach can bo")
    print("4. Thoat")


if __name__ == "__main__":
    n = int(input("Nhap so luong can bo: "))
    qlcb = QLCB()
    
    for i in range(n):
        loai = int(input("Nhap loai can bo (1: cong nhan, 2: ky su, 3: nhan vien): "))
        if loai == 1:
            cb = Congnhan()
        elif loai == 2:
            cb = Kysu()
        else:
            cb = Nhanvien()
        cb.inp()
        qlcb.themcb(cb)
    
    chon = 0
    while True:
        menu()
        chon = int(input("Nhap lua chon: "))
        if chon == 1:
            loai = int(input("Nhap loai can bo (1: cong nhan, 2: ky su, 3: nhan vien): "))
            if loai == 1:
                cb = Congnhan()
            elif loai == 2:
                cb = Kysu()
            else:
                cb = Nhanvien()
            cb.inp()
            qlcb.themcb(cb)
        elif chon == 2:
            ten = input("Nhap ten can bo can tim: ")
            qlcb.timcb(ten)
        elif chon == 3:
            qlcb.hiencb()
        elif chon == 4:
            qlcb.thoat()
            break
        else:
            print("Lua chon khong hop le. Vui long chon lai.")