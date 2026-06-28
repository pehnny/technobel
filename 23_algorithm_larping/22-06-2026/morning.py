def unique_in_order(sequence):
    solution = []
    for index, item in enumerate(sequence):
        if index == 0:
            solution.append(item)
        elif solution[-1] != item:
            solution.append(item)
    return solution

def is_triangle_number(number: int) -> bool:
    state = 0
    sequence = 0
    
    while state < number:
        sequence += 1
        state += sequence
    
    print(state)
    return number == state

def sort_array(source_array):
    odds = sorted([num for num in source_array if num % 2])
    p_odd = 0
    solution = source_array.copy()
    
    for p_num in range(len(solution)):
        if solution[p_num] % 2:
            solution[p_num] = odds[p_odd]
            p_odd += 1
    return solution

def duplicate_encode(word):
    #your code here
    lword = word.lower()
    
    occurences = {}
    for char in lword:
        if char not in occurences:
            occurences[char] = 1
        else:
            occurences[char] += 1
    
    solution = []
    for char in lword:
        if occurences[char] == 1:
            solution.append("(")
        else:
            solution.append(")")
    
    return "".join(solution)

def fizzBuzz(n: int) -> list[str]:
    solution = []

    for num in range(1, n+1):
        value = []
        if not num % 3:
            value.append('Fizz')
        if not num % 5:
            value.append('Buzz')
        if len(value) > 0:
            solution.append("".join(value))
        else:
            solution.append(str(num))
    return solution

def checkIfPangram(sentence: str) -> bool:
    visited = set()
    for char in sentence:
        visited.add(char)
    return len(visited) == 26

def CodelandUsernameValidation(strParam):
    if not 4 <= len(strParam) <= 25:
        return False
    if not strParam[0].isalpha():
        return False
    if strParam[-1] == "_":
        return False
    for char in strParam:
        if not char.isalnum() and char != "_":
            return False
    return True

def FindIntersection(strArr) -> str:
    first, second = strArr
    first, second = first.split(","), second.split(",")
    first, second = [int(num) for num in first], [int(num) for num in second]
    first, second = set(first), set(second)
    intersection = first.intersection(second)
    intersection = [str(num) for num in sorted(intersection)]
    if len(intersection) == 0:
        return "false"
    return ",".join(intersection)

def QuestionsMarks(strParam) -> str:
    left = ""
    state = ""
    hasSumToTen = False

    for char in strParam:
        if char.isdigit():
            if left == "":
                left = char
            else:
                if int(left) + int(char) == 10:
                    if state != "???":
                        return "false"
                    hasSumToTen = True
                state = ""
                left = char
        else:
            if char == "?" and left != "":
                state += char
        
    if hasSumToTen:
        return "true"
    
    return "false"

def FirstReverse(strParam):
    return strParam[::-1]

def FirstFactorial(num):
    a = 1
    b = 1
    for i in range(num):
        a, b = a*b, b+1
    return a

def LongestWord(sen):
    """Words can contain numbers !
    """
    def length(word: str) -> int:
        count = 0
        for c in word:
            if c.isalnum():
                count += 1
        return count
    
    words = sen.split()
    len_words = [length(word) for word in words]
    solution = ""
    
    for word, leng in zip(words, len_words):
        if leng > len(solution):
            solution = word[:leng]
        
    return solution
