def unique_in_order(sequence):
    if len(sequence) < 2:
        return list(sequence)
    
    print(sequence)
    solution = [sequence[0]]
    state = solution[-1]
    for element in sequence[1:]:
        if element != state:
            solution.append(element)
        state = element
    return solution

def is_triangle_number(number: int) -> bool:
    if number == 0:
        return True
    
    value = 1
    i = 1
    while value < number:
        i += 1
        value += i
    return value == number

def duplicate_encode(word):
    #your code here
    lower = word.lower()
    solution = [""]
    for c in lower:
        if lower.count(c) > 1:
            solution.append(")")
        else:
            solution.append("(")
    return "".join(solution)

def sort_array(source_array):
    odds = [value for value in source_array if value % 2]
    odds.sort()
    
    i = 0
    solution = []
    for value in source_array:
        if value % 2:
            solution.append(odds[i])
            i += 1
        else:
            solution.append(value)
    return solution


def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # The idea should be the calculate the product once
    # then divide by the current value
    # However, this is explicitly fordbidden:
    # "without using the division operation"
    # We still need the algorithm to be O(n) so
    # we have to find a way to not recalculate everything
    # on each step but not use division either.
    # Anyway, this technique may not work when a 0 appears.
    # Let's write the messy solution anyway and look at the problem
    # differently afterward
    # The idea is to transform a O(n²) to O(n). Whats' the trick ?
    # What is multiplication anyway ? Multiplication is a repeated sum.
    # This doesn't solve the problem because using division is not repeated
    # substraction.
    # Let's write the solution with O(n) but division.
    # The solution works pretty fast but does not satisfy the second condition.
    # How can I match O(n) without division ? How not to recompute
    # the whole product ? Is it even possible ?
    # It's a called a prefix-suffix pattern !
    # The idea is to accumulate de product (sum) from left
    # then from right. The complexity is O(n) but the real computation is 2n.

    # O(n²)
    # solution = []
    # for i, value in enumerate(nums):
    #     product = 1
    #     for factor in nums[:i] + nums[i+1:]:
    #         product *= factor
    #     solution.append(product)

    # zeroes = nums.count(0)
    # if zeroes > 1:
    #     return [0 for _ in nums]

    # max_product = 1
    # for value in nums:
    #     if value != 0:
    #         max_product *= value
    
    # O(n) but with division
    # solution = []
    # for value in nums:
    #     if zeroes == 1:
    #         if value != 0:
    #             solution.append(0)
    #         else:
    #             solution.append(max_product)
    #     else:
    #         solution.append(max_product // value)

    # O(n) without division
    prefix = [nums[0]]
    suffix = [nums[-1]]
    right = len(nums) - 1
    for left in range(1, len(nums)):
        right -= 1
        prefix.append(prefix[left-1]*nums[left])
        suffix.append(suffix[left-1]*nums[right])
    suffix = suffix[::-1]
    
    solution = []
    for i in range(len(nums)):
        if i == 0:
            solution.append(suffix[i+1])
        elif i == len(nums)-1:
            solution.append(prefix[i-1])
        else:
            value = prefix[i-1] * suffix[i+1]
            solution.append(value)

    # # O(n) without division and with O(1) space
    # curr_left_prod = 1
    # curr_right_prod = 1
    # answer = [1] * len(nums)
    
    # for i in range(len(nums)):
    #     answer[i] = curr_left_prod
    #     curr_left_prod = curr_left_prod * nums[i]

    # for i in range(len(nums)-1, -1, -1):
    #     answer[i] *= curr_right_prod
    #     curr_right_prod = curr_right_prod * nums[i]

    # return answer
    return solution
    

def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals.sort(key=lambda x:x[0])
    solution = [intervals[0]]
    for interval in intervals:
        start, end = interval
        previous = solution[-1]
        p_start, p_end = previous
        if start > p_end:
            solution.append(interval)
        elif end > p_end:
            solution[-1][1] = end
    return solution
    

def productExceptSelf2(nums: list[int]) -> list[int]:
    product = 1
    solution = [1 for _ in range(len(nums))]
    
    for i, value in enumerate(nums):
        solution[i] *= product
        product *= value
    
    product = 1
    l = len(nums)-1
    for i, value in enumerate(nums[::-1]):
        solution[l-i] *= product
        product *= value
    
    return solution
