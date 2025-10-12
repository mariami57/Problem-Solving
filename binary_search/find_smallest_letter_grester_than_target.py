from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        smallest = letters[0]

        while left <= right:
            mid = (left + right) // 2
            if ord(letters[mid]) > ord(target):
                right = mid - 1
                smallest = letters[mid]
            elif ord(letters[mid]) <= ord(target):
                left = mid + 1
        return smallest






print(Solution().nextGreatestLetter(letters = ["c","f","j"], target = "a"))