from typing import List


# class Solution:
#     def smallestRangeI(self, nums: List[int], k: int) -> int:
#         max_n = max(nums)
#         min_n = min(nums)
#
#         for _ in range(k):
#             max_n -= 1
#             min_n +=1
#
#             if min_n >= max_n:
#                 return 0
#         return max_n - min_n


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, (max(nums) - min(nums)) - 2*k)


print(Solution().smallestRangeI(nums = [1,3,6], k = 3))
