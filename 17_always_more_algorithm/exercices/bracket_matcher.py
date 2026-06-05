def bracket_matcher(strParam: str) -> int:
    state = 1
    for c in strParam:
        # +1 when opening
        if c == "(":
            state += 1
        # -1 when closing
        elif c == ")":
            state -= 1
        # return 0 when closing before opening
        if state < 1:
            return 0
    
    # return 1 if state unchanged (every brackets were closed correctly)
    if state == 1:
        return 1
    # return 0 otherwise (unclosed backets, ...)
    return 0
