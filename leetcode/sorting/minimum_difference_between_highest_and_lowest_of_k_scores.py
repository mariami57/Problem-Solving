from typing import List


# class Solution:
#     def minimumDifference(self, nums: List[int], k: int) -> int:
#         if k == 1:
#             return 0
#
#         nums.sort()
#         min_diff = max(nums)
#         for i in range(len(nums)-k + 1):
#             diff = abs(nums[i] - nums[i+k-1])
#             min_diff = min(min_diff, diff)
#         return min_diff

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        

print(Solution().minimumDifference(nums = [9,4,1,7], k = 2))