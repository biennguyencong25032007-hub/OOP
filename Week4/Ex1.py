class NhanVien:
    def __init__(self, ten, luong_cb, he_so, max_luong):
        self.__ten_nhan_vien = ten
        self.__luong_co_ban = luong_cb
        self.__he_so_luong = he_so
        self.LUONG_MAX = max_luong

    def get_ten_nhan_vien(self):
        return self.__ten_nhan_vien
    
    def set_ten_nhan_vien(self, ten):
        self.__ten_nhan_vien = ten
    
    def get_luong_co_ban(self):
        return self.__luong_co_ban
    
    def set_luong_co_ban(self, luong_cb):
        self.__luong_co_ban = luong_cb
    
    def get_he_so_luong(self):
        return self.__he_so_luong
    
    def set_he_so_luong(self, he_so):
        self.__he_so_luong = he_so
    
    def tinh_luong(self):
        return self.__luong_co_ban * self.__he_so_luong
    
    # tăng lương
    def tang_luong(self, muc_tang):
        # Tính nháp hệ số mới và lương mới
        he_so_moi = self.__he_so_luong + muc_tang
        luong_moi = self.__luong_co_ban * he_so_moi
        
        # Kiểm tra điều kiện vượt mức lương tối đa
        if luong_moi > self.LUONG_MAX:
            print(f"[THONG BAO] Khong the tang luong! Luong moi ({luong_moi}) vuot qua luong toi da cho phep ({self.LUONG_MAX}).")
            return False
        else:
            self.__he_so_luong = he_so_moi
            return True
    
    def in_t_tin(self):
        print("--- Thong Tin Nhan Vien ---")
        print(f"Ten nhan vien: {self.__ten_nhan_vien}")
        print(f"Luong co ban : {self.__luong_co_ban}")
        print(f"He so luong  : {self.__he_so_luong}")
        print(f"Luong toi da : {self.LUONG_MAX}")
        print(f"-> Luong hien tai: {self.tinh_luong()}")
        print("---------------------------")


if __name__ == "__main__":
    nv1 = NhanVien("Nguyen Cong Bien", 5000000, 2.0, 15000000)
    nv1.in_t_tin()
    
    print("\nYeu cau tang he so luong them 0.5...")
    if nv1.tang_luong(0.5):
        print("=> Tang luong thanh cong!")
    nv1.in_t_tin()
    
    print("\nYeu cau tang he so luong them 1.0...")
    if nv1.tang_luong(1.0):
        print("=> Tang luong thanh cong!")
    nv1.in_t_tin()