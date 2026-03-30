# Lớp cha (Base class)
class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_sx = nha_sx
        self.gia = gia

    def xuat_thong_tin(self):
        print(f"Mã hàng: {self.ma_hang} | Tên hàng: {self.ten_hang} | Nhà SX: {self.nha_sx} | Giá: {self.gia:,.0f} VNĐ")


# Lớp con: Hàng Điện Máy (kế thừa từ HangHoa)
class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        # Gọi hàm khởi tạo của lớp cha
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    # Ghi đè (Override) phương thức xuất thông tin
    def xuat_thong_tin(self):
        super().xuat_thong_tin() # In thông tin chung
        print(f"   -> Bảo hành: {self.tg_baohanh} tháng | Điện áp: {self.dien_ap}V | Công suất: {self.cong_suat}W")


# Lớp con: Hàng Sành Sứ (kế thừa từ HangHoa)
class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.loai_nguyenlieu = loai_nguyenlieu

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        print(f"   -> Loại nguyên liệu: {self.loai_nguyenlieu}")


# Lớp con: Hàng Thực Phẩm (kế thừa từ HangHoa)
class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_hethan):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_hethan = ngay_hethan

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        print(f"   -> Ngày sản xuất: {self.ngay_sx} | Ngày hết hạn: {self.ngay_hethan}")


if __name__ == "__main__":
    # 1. Tạo mỗi loại một mặt hàng cụ thể
    dien_may = HangDienMay("DM001", "Tivi Sony 4K", "Sony", 15000000, 24, 220, 150)
    sanh_su = HangSanhSu("SS001", "Bộ ấm trà hoa văn", "Gốm sứ Bát Tràng", 500000, "Đất sét trắng cao cấp")
    thuc_pham = HangThucPham("TP001", "Sữa tươi tiệt trùng", "Vinamilk", 35000, "01/10/2023", "01/04/2024")

    # 2. Xuất thông tin về các mặt hàng này
    print("--- THÔNG TIN HÀNG ĐIỆN MÁY ---")
    dien_may.xuat_thong_tin()
    print("-" * 50)

    print("--- THÔNG TIN HÀNG SÀNH SỨ ---")
    sanh_su.xuat_thong_tin()
    print("-" * 50)

    print("--- THÔNG TIN HÀNG THỰC PHẨM ---")
    thuc_pham.xuat_thong_tin()
    print("-" * 50)