class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """Failed !

        The logic is to check if every number has a predecessor (n-1).
        If it has not you start counting for consecutives (while).
        When the sequence is broken, you check if you have a new record (max_count).
        """
        set_nums = set(nums)
        max_count = 0
        for n in set_nums:
            if n - 1 not in set_nums:
                current = n
                count = 1
                while current + 1 in set_nums:
                    count += 1
                    current += 1
                if max_count < count:
                    max_count = count
        return max_count