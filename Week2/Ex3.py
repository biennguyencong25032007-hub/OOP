def ngang(n):
    for i in range(n):
        print("+ - - - - ", end="")
    print("+")

def doc(n):
    for i in range(4):
        for j in range(n):
            print("|         ", end="")
        print("|")

def luoi(n, m):
    for i in range(n):
        ngang(m)
        doc(m)
    ngang(m)

def main():
    print("2x2")
    luoi(2, 2)
    print("4x4")
    luoi(4, 4)

if __name__ == "__main__":
    main()