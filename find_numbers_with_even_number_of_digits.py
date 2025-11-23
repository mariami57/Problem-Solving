from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            num_str = str(num)

            if len(num_str) % 2 == 0:
                result += 1
        return result

print(Solution().findNumbers([12,345,2,6,7896]))