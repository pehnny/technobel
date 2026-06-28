def calculate(text: str) -> int:
    stack: list[tuple[int, int]] = []
    number = 0
    result = 0
    sign = 1

    operations = {
        "+": 1,
        "-": -1
    }

    for char in text:
        if char.isdigit():
            number = number * 10 + int(char)
        elif char in operations:
            result += sign*number
            number = 0
            sign = operations[char]
        elif char == "(":
            stack.append((result, sign))
            result = 0
            sign = 1
        elif char == ")":
            result += sign*number
            number = 0
            p_result, p_sign = stack.pop()
            result = p_result + p_sign*result           
    result += sign*number
    return result
