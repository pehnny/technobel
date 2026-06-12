"""Idée d'optimisation : garder un slicing window classique mais calculer la somme à la volée
(retirer le premier, ajouter le nouveau)
Utiliser un dictionnaire/set pour déterminer si il y a des doublons.
"""

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = []
        left = 0
        while left < len(nums)-k+1:
            right = left+k
            subnums = nums[left:right]
            visited = set()
            last_duplicate = 0
            for i in range(len(subnums)):
                value = subnums[i]
                if not value in visited:
                    visited.add(value)
                else:
                    last_duplicate = i
            if last_duplicate > 0:
                left += last_duplicate
            else:
                sums.append(sum(subnums))
                left += 1

        if len(sums) == 0:
            return 0
        return max(sums)
