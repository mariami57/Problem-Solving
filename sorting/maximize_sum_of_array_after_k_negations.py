from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=abs, reverse=True)
        sum_val = 0
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
            sum_val += nums[i]

        if k % 2 == 1:
            sum_val -= 2 * abs(nums[-1])

        return sum_val

print(Solution().largestSumAfterKNegations(nums=[4, 2, 3], k=1))
print(Solution().largestSumAfterKNegations(nums = [3,-1,0,2], k = 3))
print(Solution().largestSumAfterKNegations(nums = [2,-3,-1,5,-4], k = 2))
