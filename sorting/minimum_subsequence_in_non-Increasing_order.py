from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        min_max_sum = 0
        rest_sum = sum(nums)
        i = 0
        result = []

        while min_max_sum <= rest_sum:
            min_max_sum += nums[i]
            rest_sum -= nums[i]
            result.append(nums[i])
            i += 1

        return result

print(Solution().minSubsequence([4,4,7,6,7]))
print(Solution().minSubsequence([4,3,10,9,8]))

