def main():
    sec = 42 * 60 + 42
    print(sec)

    miles = 10 / 1.61
    print(f"{miles:.2f}")

    secpm = sec / miles
    mn_pace = int(secpm // 60)
    mn_sec = int(secpm % 60)

    hours = sec / 3600.0
    avg_mph = miles / hours

    print(mn_pace, mn_sec)
    print(avg_mph)

if __name__ == "__main__":
    main()

