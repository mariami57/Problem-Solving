from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        result = [0] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        return result



print(Solution().sortedSquares(nums = [-5,-3,-2,-1]))
print(Solution().sortedSquares(nums = [-4,-1,0,3,10]))