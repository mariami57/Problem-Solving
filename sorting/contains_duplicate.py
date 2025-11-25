from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1 or not nums:
            return False

        nums.sort()


        for i in range(len(nums) -1, -1, -1):
            if nums[i] == nums[i - 1]:
                return True

        return False

print(Solution().containsDuplicate([1,2,3,4]))

