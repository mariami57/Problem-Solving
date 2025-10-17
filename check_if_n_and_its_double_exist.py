from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            double = num * 2
            half = num // 2
            if double in seen or (num % 2 == 0 and half in seen):
                return True
            seen.add(num)
        return False
print(Solution().checkIfExist([7,1,14,11]))