from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        result = 0
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for k, v in counts.items():
            if v == 2:
                result ^= k
        return result

print(Solution().duplicateNumbersXOR([1,2,1,3]))
print(Solution().duplicateNumbersXOR([1,2,3]))
print(Solution().duplicateNumbersXOR([1,2,2,1]))
