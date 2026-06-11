class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = []
        for i in range(len(nums)-k):
            high = i+k+1
            subnums = nums[i:high]
            subnums_count = [subnums.count(value) for value in subnums]
            duplicate = max(subnums_count)
            if duplicate == 1:
                sums.append(sum(subnums))
        if len(sums) == 0:
            return 0
        
        return max(sums)