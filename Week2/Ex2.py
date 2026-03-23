import math

def solve1():
    r = 5
    pi = 3.14
    volume = (4 * (pi * pow(r, 3))) / 3
    print(f"{volume:.2f}")

def solve2():
    cover = 24.95
    disc_price = cover * 0.6
    ship = 3 + (59 * 0.75)
    total = (disc_price * 60) + ship
    print(total)

def solve3():
    st = (6 * 3600) + (52 * 60)
    easy = (8 * 60) + 15
    tempo = (7 * 60) + 12
    tong = 2 * easy + 3 * tempo
    end = st + tong
    print(f"{end // 3600}:{(end % 3600) // 60}")

def main():
    solve1()
    solve2()
    solve3()

if __name__ == "__main__":
    main()

