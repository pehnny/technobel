def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in groups:
            groups[sorted_word] = [word]
        else:
            groups[sorted_word].append(word)
    return [groups[group] for group in groups]
