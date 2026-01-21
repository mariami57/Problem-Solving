from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)

        for i in range(len(nums)):
            if nums[i] * 2 <= max_num or nums[i] == max_num:
                continue
            return -1

        return nums.index(max_num)

print(Solution().dominantIndex([3,6,1,0]))
print(Solution().dominantIndex([1,2,3,4]))