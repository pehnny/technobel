def valid_parentheses(text: str) -> bool:
    if len(text) % 2:
        return False
    
    parentheses = {
        ")":"(",
        "]": "[",
        "}": "{"
    }
    stack: list[str] = []

    for c in text:
        if c not in list(parentheses) + list(parentheses.values()):
            return False
        if c in list(parentheses):
            if len(stack) == 0:
                return False
            previous = stack.pop()
            if previous != parentheses[c]:
                print()
                return False
        else:
            stack.append(c)
    return len(stack) == 0