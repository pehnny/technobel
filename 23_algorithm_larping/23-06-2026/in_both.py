"""
CHALLENGE 10

Two warehouses each send a list of the product IDs they currently stock.
The buying team wants the products that are available in BOTH warehouses,
listed once each (no duplicates).

To keep the output predictable, return the common product IDs sorted in
ascending order.

Examples:
    in_both([1, 2, 2, 1], [2, 2])       -> [2]
    in_both([4, 9, 5], [9, 4, 9, 8, 4]) -> [4, 9]

"""

from testkit import check, report


def in_both(left, right):
    return sorted(list(set(left).intersection(set(right))))


if __name__ == "__main__":
    check("single common", in_both([1, 2, 2, 1], [2, 2]), [2])
    check("two common", in_both([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])
    check("nothing shared", in_both([1, 2, 3], [4, 5, 6]), [])
    check("one empty", in_both([], [1, 2]), [])
    check("both empty", in_both([], []), [])
    check("all duplicates", in_both([1, 1, 1], [1, 1]), [1])
    check("same set", in_both([1, 2, 3], [3, 2, 1]), [1, 2, 3])
    report()
