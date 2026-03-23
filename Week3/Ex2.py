class Sieunhan:
    def __init__(self, ten, vukhi, mausac):
        self.ten = ten
        self.vukhi = vukhi
        self.mausac = mausac
    
    def output(self):
        print(f"Ten: {self.ten} | Vu khi: {self.vukhi} | Mau sac: {self.mausac}")

def main():
    sn1 = Sieunhan("Gao", "Sức mạnh siêu phàm", "Đỏ")
    sn2 = Sieunhan("Điện quang", "Trí tuệ và kỹ năng chiến đấu", "Vàng")
    sn1.output()
    sn2.output()

if __name__ == "__main__":
    main()