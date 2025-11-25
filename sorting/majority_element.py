from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_count = {}

        for num in nums:
           nums_count[num] = nums_count.get(num, 0) + 1

        return max(nums_count, key = nums_count.get)


print(Solution().majorityElement([3,2,3]))
