class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = []
        for i in range(len(nums)-k+1):
            high = i+k
            subnums = nums[i:high]
            duplicate = max([subnums.count(value) for value in subnums])
            if duplicate == 1:
                sums.append(sum(subnums))
        if len(sums) == 0:
            return 0
        
        return max(sums)