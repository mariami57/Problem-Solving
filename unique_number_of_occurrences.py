from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        number_of_occurrences = {}
        for char in arr:
            number_of_occurrences[char] = number_of_occurrences.get(char, 0) + 1

        occurrences = set(number_of_occurrences.values())
        if len(occurrences) == len(number_of_occurrences):
            return True
        else:
            return False

arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(Solution().uniqueOccurrences(arr))
