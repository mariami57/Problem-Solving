from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dupe, missing = -1, -1

        for i in range(1,len(nums) + 1):
            count = nums.count(i)
            if count == 2:
                dupe = i
            elif count == 0:
                missing = i

        return [dupe,missing]

print(Solution().findErrorNums([1,1]))
print(Solution().findErrorNums([1,3,3]))
print(Solution().findErrorNums([3,2,3,4,6,5]))
print(Solution().findErrorNums([3,2,2]))
print(Solution().findErrorNums([1,2,2,4]))

