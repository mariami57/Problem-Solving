from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        curr_length = 0

        for num in nums:
            if num == 1:
                curr_length += 1
            else:
                max_length = max(max_length, curr_length)
                curr_length = 0
        max_length = max(max_length, curr_length)
        return max_length

print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(Solution().findMaxConsecutiveOnes([1,0,1,1,0,1]))