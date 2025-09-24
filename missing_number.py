from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        unique=[]
        for i in range(len(nums)+1):
            unique.append(i)

        for j in range(len(unique)):
            if j not in nums:
                return j

print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))