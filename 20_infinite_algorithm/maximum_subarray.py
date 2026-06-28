"""Idée d'optimisation : garder un slicing window classique mais calculer la somme à la volée
(retirer le premier, ajouter le nouveau)
Utiliser un dictionnaire/set pour déterminer si il y a des doublons.
"""

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        left = 0
        state = 0
        result = 0
        duplicate = {}
        for right in range(len(nums)):
            value = nums[right]
            state += value

            if value not in duplicate:
                duplicate[value] = 1
            else:
                duplicate[value] += 1

            # Attention, quand right - left = k, la window est nums[left:right+1] car le state est évalué avant
            if right - left == k:
                previous = nums[left]
                state -= previous

                duplicate[previous] -= 1
                if duplicate[previous] == 0:
                    del duplicate[previous]

                left +=1

            # En conséquence, le check de la somme sans doublon doit se faire en dehors du shrink.
            # Si on place la vérification dans le shrink, les cas où la solution se trouve dans la première window sont manqués.
            # Exemple : [1, 2, 2] -> [1, 2] -> 3 serait un cas manqué.
            if len(duplicate) == k:
                result = max(state, result)
        return result
