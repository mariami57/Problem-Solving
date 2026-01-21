from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        result = [0] * len(nums)

        pos = len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1


        return result

print(Solution().sortedSquares(nums = [-5,-3,-2,-1]))
print(Solution().sortedSquares(nums = [-4,-1,0,3,10]))

