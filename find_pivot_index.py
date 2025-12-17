from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            if left_sum == right_sum:
                return i
        return -1

print(Solution().pivotIndex([2,1,-1]))
print(Solution().pivotIndex([1,7,3,6,5,6]))
print(Solution().pivotIndex([1,2,3]))
