def fizzbuzz(maximum : int) -> None:
    for i in range(1, maximum+1):
        value: list[str] = []
        if not i % 3:
            value.append("Fizz")
        if not i % 5:
            value.append("Buzz")
        if len(value) > 0:
            print("".join(value))
        else:
            print(i)
    return