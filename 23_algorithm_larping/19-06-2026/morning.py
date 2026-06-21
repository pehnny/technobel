class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        visited = set()
        left = 0
        for right in range(len(nums)):
            current = nums[right]
            if current not in visited:
                visited.add(current)
                if right - left > 0:
                    nums[right] = nums[left]
                    nums[left] = current
                left += 1
        return len(visited)
    
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        visited = {}
        for value in nums:
            if value not in visited:
                visited[value] = 1
            else:
                visited[value] += 1
        return max(visited, key=lambda k:visited[k])

# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         max_profit = 0
#         left = 0
#         visited = set()
#         for i, buy in enumerate(prices[:-1]):
#             if buy not in visited:
#                 visited.add(buy)
#                 for sell in prices[i+1:]:
#                     profit = sell - buy
#                     if profit > max_profit:
#                         max_profit = profit
#         return max_profit

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        minimum = prices[0]
        for i, buy in enumerate(prices[:-1]):
            if buy <= minimum:
                minimum = buy
            else:
                profit = buy - minimum
                max_profit = max(max_profit, profit)
        return max_profit
    
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            current = nums[right]
            if current != 0:
                if right - left > 0:
                    nums[right] = nums[left]
                    nums[left] = current
                left += 1
        return

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        distance = len(nums)
        visited = {}
        for i, value in enumerate(nums):
            if value in visited:
                distance = i - visited[value]
                if distance <= k:
                    return True
            visited[value] = i
        return False

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        reference = min(strs, key=lambda word:len(word))
        for i, c in enumerate(reference):
            for word in strs:
                if c != word[i]:
                    return prefix
            prefix += c
        return prefix
