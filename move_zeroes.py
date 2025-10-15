from typing import List


# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 nums.remove(nums[i])
#                 nums.append(0)
#

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        next_idx = 0

        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[idx], nums[next_idx] = nums[next_idx], nums[idx]
                next_idx += 1
                
print(Solution().moveZeroes([1,0,1]))