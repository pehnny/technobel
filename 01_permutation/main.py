def main() -> None:
    a, b = 7, 5
    print(a,b)
    a, b = b, a
    print(a,b)

if __name__ == "__main__":
    main()