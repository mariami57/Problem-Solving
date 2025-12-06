from typing import List


# class Solution:
#     def duplicateNumbersXOR(self, nums: List[int]) -> int:
#         result = 0
#         counts = {}
#         for num in nums:
#             counts[num] = counts.get(num, 0) + 1
#
#         for k, v in counts.items():
#             if v == 2:
#                 result ^= k
#         return result

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res = 0
        seen = set()

        for num in nums:
            if num in seen:
                res ^= num
            else:
                seen.add(num)
        return res

print(Solution().duplicateNumbersXOR([1,2,1,3]))
print(Solution().duplicateNumbersXOR([1,2,3]))
print(Solution().duplicateNumbersXOR([1,2,2,1]))
