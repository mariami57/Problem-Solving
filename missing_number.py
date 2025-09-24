from typing import List


# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         unique=[]
#         for i in range(len(nums)+1):
#             unique.append(i)
#
#         for j in range(len(unique)):
#             if j not in nums:
#                 return j

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n+1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


print(Solution().missingNumber([3,0,1]))