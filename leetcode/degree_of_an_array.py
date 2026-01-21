from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        count = {}
        left = {}
        right = {}

        for i, num in enumerate(nums):
            count[num] = count.get(num, 0) + 1
            if num not in left:
                left[num] = i
            right[num] = i

        degree = max(count.values())
        res = float('inf')
        for num in count:
            if count[num] == degree:
                res = min(res, right[num] - left[num] + 1)
        return res

print(Solution().findShortestSubArray([1,2,2,3,1]))
print(Solution().findShortestSubArray([1,2,2,3,1,4,2]))


