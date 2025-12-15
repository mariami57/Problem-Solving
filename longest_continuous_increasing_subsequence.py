from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_sub = 0
        curr_sub = 1
        i = 0
        j = 1

        while i < j and j < len(nums):
            if nums[i] < nums[j]:
                curr_sub += 1
                j += 1
                i += 1
            else:
                max_sub = max(max_sub, curr_sub)
                curr_sub = 1
                i = j
                j += 1


        return max(max_sub, curr_sub)
print(Solution().findLengthOfLCIS([3,0,6,2,4,7,0,0]))
print(Solution().findLengthOfLCIS([1,3,5,4,7]))
print(Solution().findLengthOfLCIS([2,2,2,2,2]))
print(Solution().findLengthOfLCIS([1,3,5,7]))



