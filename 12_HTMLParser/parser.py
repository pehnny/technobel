def parser(text: str) -> bool | str:
    # Trivial
    if len(text) == 0:
        return True

    # Initialize stack and conditions
    valid = set(["b", "p", "i", "a", "div"])
    stack: list[str] = []

    # Split (without regex)
    chars: list[str] = []
    tags: list[str] = []
    for c in text:
        chars.append(c)
        if c == ">":
            tags.append("".join(chars))
            chars = []

    # Check
    for tag in tags:
        value = tag[1:-1]
        is_closing = value[0] == "/"
        value = value.lstrip("/")

        # False if invalid tag
        if value not in valid:
            return False
        
        # Check if closing tag
        if is_closing:
            # Closing without opening
            if len(stack) == 0:
                return False
            # Wrongly closed
            previous = stack.pop()
            if previous != value:
                return previous
        # Append stack with opening
        else:    
            stack.append(value)
    return not stack
