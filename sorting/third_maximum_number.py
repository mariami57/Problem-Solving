from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_nums = {}

        for num in nums:
            max_nums[num] = max_nums.get(num, 0) + 1
        #
        max_sorted = sorted(max_nums.items(), key=lambda x: -x[0])

        if len(max_sorted) >= 3:
            return max_sorted[2][0]
        else:
            return max(max_nums, key = lambda x: x)


print(Solution().thirdMax([1,2,2,5,3,5]))
print(Solution().thirdMax([1, 2]))
print(Solution().thirdMax([2,2,3,1]))
print(Solution().thirdMax([3,2,1]))



