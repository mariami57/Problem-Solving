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

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         expected_sum = n * (n+1) // 2
#         actual_sum = sum(nums)
#         return expected_sum - actual_sum


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        lo,hi = 0, len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > mid:
                hi = mid
            else:
                lo = mid + 1
        return lo

print(Solution().missingNumber([3,0,1]))