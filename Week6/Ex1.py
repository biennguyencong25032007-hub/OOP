from abc import ABC, abstractmethod
import pickle
import os

class GiaKhongHopLe(Exception):
    pass

class MaHangTrungLap(Exception):
    pass

class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, gia):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self.gia = gia

    @property
    def ma_hang(self):
        return self._ma_hang

    @property
    def ten_hang(self):
        return self._ten_hang

    @property
    def gia(self):
        return self._gia

    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe(f"Giá '{value}' không hợp lệ. Giá phải >= 0.")
        self._gia = value

    @abstractmethod
    def loai_hang(self):
        pass

    @abstractmethod
    def inTTin(self):
        pass

    def __str__(self):
        return f"Mã: {self.ma_hang: <5} | Tên: {self.ten_hang: <15} | Giá: {self.gia: >10,}"

    def __eq__(self, other):
        if isinstance(other, HangHoa):
            return self.ma_hang == other.ma_hang
        return False

    def __lt__(self, other):
        return self.gia < other.gia

    def __hash__(self):
        return hash(self.ma_hang)

class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, thoi_gian_bh):
        super().__init__(ma_hang, ten_hang, gia)
        self.thoi_gian_bh = thoi_gian_bh

    def loai_hang(self):
        return "Điện Máy"

    def inTTin(self):
        return f"[{self.loai_hang(): ^10}] {super().__str__()} | Bảo hành: {self.thoi_gian_bh} tháng"

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, nha_san_xuat):
        super().__init__(ma_hang, ten_hang, gia)
        self.nha_san_xuat = nha_san_xuat

    def loai_hang(self):
        return "Sành Sứ"

    def inTTin(self):
        return f"[{self.loai_hang(): ^10}] {super().__str__()} | NSX: {self.nha_san_xuat}"

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, ngay_het_han):
        super().__init__(ma_hang, ten_hang, gia)
        self.ngay_het_han = ngay_het_han

    def loai_hang(self):
        return "Thực Phẩm"

    def inTTin(self):
        return f"[{self.loai_hang(): ^10}] {super().__str__()} | HSD: {self.ngay_het_han}"

class QuanLyHangHoa:
    def __init__(self):
        self.danh_sach = []

    def them_hang(self, sp):
        if any(h == sp for h in self.danh_sach):
            raise MaHangTrungLap(f"Lỗi: Mã hàng '{sp.ma_hang}' đã tồn tại trong hệ thống!")
        self.danh_sach.append(sp)
        print(f"-> Đã thêm thành công: {sp.ten_hang}")

    def hien_thi(self):
        print("\n--- DANH SÁCH HÀNG HÓA ---")
        for sp in self.danh_sach:
            print(sp.inTTin())
        print("-" * 30)

    def xep_theo_gia(self):
        self.danh_sach = sorted(self.danh_sach)
        print("-> Đã sắp xếp danh sách theo giá tăng dần.")

    def luu_file(self, ten_file="data_hanghoa.pkl"):
        with open(ten_file, 'wb') as f:
            pickle.dump(self.danh_sach, f)
        print(f"-> Đã lưu dữ liệu vào file {ten_file}")

    def doc_file(self, ten_file="data_hanghoa.pkl"):
        if os.path.exists(ten_file):
            with open(ten_file, 'rb') as f:
                self.danh_sach = pickle.load(f)
            print(f"-> Đã đọc dữ liệu từ file {ten_file}")
        else:
            print("-> File không tồn tại, tạo danh sách mới.")

if __name__ == "__main__":
    ql = QuanLyHangHoa()

    try:
        sp1 = HangDienMay("DM01", "Tivi Sony", 15000000, 24)
        sp2 = HangSanhSu("SS01", "Bát tràng", 50000, "Gốm Bát Tràng")
        sp3 = HangThucPham("TP01", "Sữa tươi", 35000, "30/12/2026")
        sp4 = HangDienMay("DM02", "Tủ lạnh LG", 8000000, 12)

        ql.them_hang(sp1)
        ql.them_hang(sp2)
        ql.them_hang(sp3)
        ql.them_hang(sp4)

        print("\n[Test] Thử tạo sản phẩm giá âm:")
        sp_loi = HangDienMay("DM03", "Máy giặt", -5000, 12)
    except GiaKhongHopLe as e:
        print(f"BẮT LỖI: {e}")

    try:
        print("\n[Test] Thử thêm sản phẩm trùng mã (DM01):")
        sp_trung = HangDienMay("DM01", "Tivi Khác", 1000, 12)
        ql.them_hang(sp_trung)
    except MaHangTrungLap as e:
        print(f"BẮT LỖI: {e}")

    ql.hien_thi()

    ql.xep_theo_gia()
    ql.hien_thi()

    print("\n[Test] File I/O:")
    ql.luu_file()
    
    ql_moi = QuanLyHangHoa()
    ql_moi.doc_file()
    print("\nHiển thị danh sách từ file đã đọc:")
    ql_moi.hien_thi()