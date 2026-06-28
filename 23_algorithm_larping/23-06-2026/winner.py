"""
CHALLENGE 11

After an online poll, every vote is a candidate ID. One candidate won by
a strict majority, meaning their ID appears more than half the time in
the list of votes. Return the winning candidate ID.

You may assume such a majority always exists.

Examples:
    winner([3, 2, 3])             -> 3
    winner([2, 2, 1, 1, 1, 2, 2]) -> 2

"""

from testkit import check, report


def winner(votes):
    return sorted(votes)[len(votes)//2]


if __name__ == "__main__":
    check("simple majority", winner([3, 2, 3]), 3)
    check("more votes", winner([2, 2, 1, 1, 1, 2, 2]), 2)
    check("single vote", winner([1]), 1)
    check("unanimous", winner([5, 5, 5, 5]), 5)
    check("majority is zero", winner([0, 0, 1]), 0)
    check("just over half", winner([7, 7, 7, 1, 2]), 7)
    report()
