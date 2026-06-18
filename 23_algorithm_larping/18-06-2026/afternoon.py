def unique_permutations[T](items: list[T]) -> list[list[T]]:
    stack: list[T] = []
    solutions: list[list[T]] = []
    
    def backtrack(items: list[T], max_length: int) -> None:
        if len(stack) == max_length:
            if stack not in solutions:
                solutions.append(stack.copy())
            return
        
        for i, item in enumerate(items):
            stack.append(item)
            backtrack(items[:i] + items[i+1:], max_length)
            stack.pop()
        return

    backtrack(items, len(items))
    return solutions

if __name__ == "__main__":
    tests = (
        ["a", "b", "a"],
        [1, 2, 2],
    )

    solutions = (
        [
            ["a", "a", "b"],
            ["a", "b", "a"],
            ["b", "a", "a"]
        ],
        [
            [1, 2, 2],
            [2, 1, 2],
            [2, 2, 1]
        ]
    )

    for test, solution in zip(tests, solutions):
        answer = unique_permutations(test)

        success = True
        if len(answer) != len(solution):
            success = False
        for item in answer:
            if item not in solution:
                success = False

        if success:
            print("Test succesful")
        else:
            print(f"Expected : {solution}, got : {answer}")
