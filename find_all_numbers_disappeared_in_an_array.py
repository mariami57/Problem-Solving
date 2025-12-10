from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        result = []

        for i, num in enumerate(nums, 1):
            if num > 0:
                result.append(i)

        return result

print(Solution().findDisappearedNumbers([1,1]))
print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
