def inverse(a: int, b: int) -> tuple[int, int]:
    a = a + b
    b = a - b
    a = a - b
    return a, b

def secondstodayshoursminutesseconds(time: int) -> tuple[int, int, int, int]:
    """division entière par rapport aux unités "du dessous" et reste par rapport aux
    unités "du dessus".
    """
    days = time // (60*60*24)
    hours = time // (60*60) % 24
    minutes = time // 60 % 60 % 24
    seconds = time % 60 % 60 % 24
    return (days, hours, minutes, seconds)

def main() -> None:
    a = 12
    b = 3*a+8
    c = b-2*a
    d = (c+25)*b
    e = (a+b)%10
    f = (c*d)//(b+6)
    g = (d+e)//(f-9)

    print(a, b, c, d, e, f, g, sep="\n")

    a, b, c = 13, 5, True
    d = not c

    print(a > 10 and b < 20)
    print(c != 40 or d >= 100)
    print(a == 2 and not b > 15)
    print(c > 50 or not d < 200)
    print((a < b and c > 30) or d == 270)
    print(not (a*b) > 100)
    print(b == 15 or (c > 60 and a < 5))
    print((b == 15 or (c > 60 and a < 5) and a < b) or not (b == 9))

    a, b = inverse(a, b)

    days, hours, minutes, seconds = secondstodayshoursminutesseconds(4561)
    print(f"days: {days}, hours: {hours}, minutes: {minutes}, seconds: {seconds}")
    return

if __name__ == "__main__":
    main()