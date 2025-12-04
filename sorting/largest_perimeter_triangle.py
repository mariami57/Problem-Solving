from typing import List

# Perimeter of triangle = P = a + b + c
# In mathematics, the triangle inequality states that for any triangle,
# the sum of the lengths of any two sides
# must be greater than or equal to the length of the remaining side.

# class Solution:
#     def largestPerimeter(self, nums: List[int]) -> int:
#         if len(nums) < 3:
#             return 0
#         nums.sort()
#         perimeter = 0
#         i = 0
#         j = 2
#
#         while j < len(nums) and i < len(nums):
#             if nums[i] + nums[i+1] > nums[j]:
#                 perimeter = max(perimeter,nums[i] + nums[i+1] + nums[j])
#             i += 1
#             j += 1
#         return perimeter

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        perimeter = 0

        for i in range(len(nums)-1, 1, -1):
            if nums[i] < nums[i-1] + nums[i-2]:
                perimeter = max(perimeter,nums[i] + nums[i-1] + nums[i-2])
        return perimeter

print(Solution().largestPerimeter([1,2,2,4,18,8]))
print(Solution().largestPerimeter([1,2,1,10]))
print(Solution().largestPerimeter([2,1,2]))

