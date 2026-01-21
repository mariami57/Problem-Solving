from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []


        for n in nums:
            index = abs(n) - 1
            nums[index] = -abs(nums[index])

        for i, num in enumerate(nums, 1):
            if num > 0:
                result.append(i)

        return result





print(Solution().findDisappearedNumbers([1,1]))
print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
