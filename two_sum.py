from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int):

        for i in range(len(nums)):
            x = target - nums[i]
            if x in nums and nums.index(x) != i:
                return [nums.index(x), i]

nums = [2,7,11,15]
target = 9

two_sum = Solution().twoSum(nums, target)
print(two_sum)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []

nums = [2,7,11,15]
target = 9

two_sum = Solution().twoSum(nums, target)
print(two_sum)