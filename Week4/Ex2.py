class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def input(self):
        coords = input().split()
        self._x = int(coords[0])
        self._y = int(coords[1])

    def display(self):
        print(f"({self._x}, {self._y})", end="")


class LineSegment:
    # Constructor mặc định
    def __init__(self, d1=None, d2=None, x1=None, y1=None, x2=None, y2=None):
        # Constructor mặc định: LineSegment()
        if d1 is None and d2 is None and x1 is None:
            self.d1 = Point(8, 5)
            self.d2 = Point(1, 0)
        # Constructor 2 Point: LineSegment(Point, Point)
        elif isinstance(d1, Point) and isinstance(d2, Point):
            self.d1 = d1
            self.d2 = d2
        # Constructor 4 số: LineSegment(int, int, int, int)
        elif x1 is not None and y1 is not None and x2 is not None and y2 is not None:
            self.d1 = Point(x1, y1)
            self.d2 = Point(x2, y2)
        # Copy constructor: LineSegment(LineSegment)
        elif isinstance(d1, LineSegment) and d2 is None:
            self.d1 = Point(d1.d1._x, d1.d1._y)
            self.d2 = Point(d1.d2._x, d1.d2._y)

    # Hàm nhập
    def input(self):
        print("Nhap diem d1 (x y): ", end="")
        self.d1.input()
        print("Nhap diem d2 (x y): ", end="")
        self.d2.input()

    def display(self):
        print("Doan thang: ", end="")
        self.d1.display()
        print(" -> ", end="")
        self.d2.display()
        print()


if __name__ == "__main__":
    a = LineSegment()

    print("=== Nhap doan thang ===")
    a.input()

    print("=== Ket qua ===")
    a.display()