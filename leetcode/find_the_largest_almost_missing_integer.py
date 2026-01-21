from collections import defaultdict
from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        n = len(nums)

        if n == k:
            return max(nums)

        for i in range(n - k + 1):
            for j in range(k):
                freq[nums[i+j]] += 1

        res = -1
        for num, count in freq.items():
            if count == 1:
                res = max(res,num)

        return res

print(Solution().largestInteger(nums = [3,9,2,1,7], k = 3))