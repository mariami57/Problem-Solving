from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        ans = len(nums)


        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < k:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
        return ans

print(Solution().minOperations([39,100,81,98,59,39,20,25], 39))