"""
CHALLENGE 15

A subscription plan is paid with exactly two coupons whose values add up
to the plan price. The coupon values are stored sorted in ascending
order. Return the 1-based positions of the two coupons that sum to the
price.

Return the positions as a list [i, j] with i < j (counting from 1).
There is at most one valid pair; if none works, return an empty list.

Examples:
    coupon_pair([2, 7, 11, 15], 9) -> [1, 2]
    coupon_pair([2, 3, 4], 6)      -> [1, 3]

"""

from testkit import check, report


def coupon_pair(values, price):
    visited = {}
    for i, value in enumerate(values):
        difference = price - value
        if difference in visited:
            return [visited[difference], i+1]
        if value not in visited:
            visited[value] = i+1
    return []


if __name__ == "__main__":
    check("first two", coupon_pair([2, 7, 11, 15], 9), [1, 2])
    check("ends", coupon_pair([2, 3, 4], 6), [1, 3])
    check("with negative", coupon_pair([-1, 0], -1), [1, 2])
    check("last two", coupon_pair([1, 2, 3, 4, 5], 9), [4, 5])
    check("no pair", coupon_pair([1, 2, 3], 100), [])
    check("single coupon", coupon_pair([5], 5), [])
    check("empty coupons", coupon_pair([], 10), [])
    report()
