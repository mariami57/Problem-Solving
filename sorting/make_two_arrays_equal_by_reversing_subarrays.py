from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()

        if target == arr:
            return True
        return False

print(Solution().canBeEqual(target = [3,7,9], arr = [3,7,11]))
print(Solution().canBeEqual(target = [7], arr = [7]))
