def longest_word(text: str) -> str:
    if text == "":
        return ""
    
    word = ""
    robert: list[str] = [word]

    for c in text:
        if c == " ":
            if len(word) > len(robert[-1]):
                robert.append(word)
            word = ""
        else:
            word += c
    
    if len(word) > len(robert[-1]):
        robert.append(word)
        word = ""
    return robert[-1]