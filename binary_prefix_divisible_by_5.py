from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        current_mod = 0

        for bit in nums:
            current_mod = (current_mod * 2 + bit) % 5

            result.append(current_mod == 0)
        return result





print(Solution().prefixesDivBy5([1,1,1]))