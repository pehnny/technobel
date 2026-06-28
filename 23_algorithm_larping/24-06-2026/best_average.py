"""
CHALLENGE 24

A monitoring tool reports the best average load over any window of k
consecutive minutes. Given the per-minute load values and the window
size k, return the highest average of any k consecutive values.

You may assume k is at least 1 and no larger than the number of values.
Return the average as a float.

Examples:
    best_average([1, 12, -5, -6, 50, 3], 4) -> 12.75
    best_average([5], 1)                     -> 5.0

"""

from testkit import check, report


def best_average(loads, k):
    maximum = sum(loads[:k])
    state = sum(loads[:k])
    left = 0
    right = k
    while right < len(loads):
        current = state + loads[right] - loads[left]
        maximum = max(current, maximum)
        right += 1
        left += 1
    return maximum / k


if __name__ == "__main__":
    check("window of four", best_average([1, 12, -5, -6, 50, 3], 4), 12.75)
    check("single value", best_average([5], 1), 5.0)
    check("window of one", best_average([0, 4, 0, 3, 2], 1), 4.0)
    check("all negative", best_average([-1, -2, -3, -4], 2), -1.5)
    check("uniform", best_average([1, 1, 1, 1], 2), 1.0)
    check("whole array", best_average([7, 4, 4], 3), 5.0)
    report()
