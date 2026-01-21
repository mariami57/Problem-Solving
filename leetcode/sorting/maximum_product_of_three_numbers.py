from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])

print(Solution().maximumProduct([-100,-98,-1,2,3,4]))
print(Solution().maximumProduct([1,2,3,4]))
print(Solution().maximumProduct([1,2,3]))