"""
CHALLENGE 13

A spreadsheet column lists daily sales figures, but the days with no
sales (zeros) should be pushed to the bottom of the column while keeping
every non-zero figure in its original order. Modify the list so all
zeros sit at the end, and return the list.

Examples:
    sink_zeros([0, 1, 0, 3, 12]) -> [1, 3, 12, 0, 0]
    sink_zeros([4, 0, 5, 0, 0, 6]) -> [4, 5, 6, 0, 0, 0]

"""

from testkit import check, report


def sink_zeros(figures):
    if len(figures) < 2:
        return figures
    # Solution space greedy
    # non_zero = [value for value in figures if value != 0]
    # figures[:len(non_zero)] = non_zero
    # figures[len(non_zero):] = [0 for _ in range(len(figures)-len(non_zero))]
    # return figures
    # Oh boy I hate bubble sort
    left = 0
    for right in range(len(figures)):
        current = figures[right]
        if current != 0:
            if right - left > 0:
                figures[right] = figures[left]
                figures[left] = current
            left += 1
    return figures


if __name__ == "__main__":
    check("mixed", sink_zeros([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
    check("several zeros", sink_zeros([4, 0, 5, 0, 0, 6]), [4, 5, 6, 0, 0, 0])
    check("all zeros", sink_zeros([0, 0, 0]), [0, 0, 0])
    check("no zeros", sink_zeros([1, 2, 3]), [1, 2, 3])
    check("empty", sink_zeros([]), [])
    check("single zero", sink_zeros([0]), [0])
    report()
