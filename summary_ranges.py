from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result = []
        i = 0

        while i < len(nums):
            start = nums[i]
            j = i
            while j + 1 < len(nums) and nums[j+1] == nums[j] + 1:
                j+=1
            if nums[j] == start:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[j]}")

            i = j+1
        return result


print(Solution().summaryRanges([0,2,3,4,6,8,9]))
print(Solution().summaryRanges([0,1,2,4,5,7]))
