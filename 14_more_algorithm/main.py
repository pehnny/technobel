import random
import exercices


def main() -> None:
    # reverse_string
    test = "Hello world !"
    solution = "! dlrow olleH"
    print(f"reverse string is successful: {solution == exercices.exercice1(test)}")

    # count_vowels
    solution = 3
    print(f"count_vowels is successful: {solution == exercices.exercice2(test)}")
    
    # palindrome
    tests = ["Bonjour", "Radar", "La mariee ira mal", "Le mercredi tout est permi"]
    solutions = [False, True, True, False]
    for test, solution in zip(tests, solutions):
        print(f"Is {test} a palindrome ? {exercices.exercice3(test)}")
        print(f"Test is successful : {exercices.exercice3(test) == solution}")

    # find_max
    test = [random.randint(0, 100) for _ in range(100)]
    solution = max(*test)
    print(f"find_max is successful: {solution == exercices.exercice4(test)}")

    # count_occurences
    test = [random.randint(0, 10) for _ in range(100)]
    solution = test.count(5)
    print(f"count_occurences is successful: {solution == exercices.exercice5(test, 5)}")

    # fizzbuzz
    exercices.exercice6(100)

    # valid_parenthese
    test = "".join([random.choice([r"(", r")", r"[", r"]", r"{", r"}"]) for _ in range(10)])
    while not exercices.exercice7(test):
        print(test)
        test = "".join([random.choice([r"(", r")", r"[", r"]", r"{", r"}"]) for _ in range(10)])
        print(f"parentheses are valid : {False}")

    print(test)
    print(f"parentheses are valide : {True}")

    # find_duplicate
    test = [random.randint(0, 10) for _ in range(5)]
    print(test)
    print("Duplicates are :", exercices.exercice8(test))

    # longest_word
    test = (["".join(["a" for _ in range(random.randint(0, 10))]) for _ in range(5)])
    solution = max(*test, key=lambda word:len(word))
    print(f"longest_word is: {exercices.exercice9(" ".join(test))} expected: {solution}")

    # two_sum
    test = [i for i in range(10)]
    test_target = 13
    solution = (4, 9)
    print(f"Expected: {solution}, got: {exercices.exercice10(test, test_target)}")
    return

if __name__ == "__main__":
    main()