from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        result = []

        for i in range(len(nums)):
            idx = sorted_nums.index(nums[i])
            if idx == 0:
                result.append(0)
            elif sorted_nums[idx-1] <= sorted_nums[idx]:
                result.append(idx)
            else:
                result.append(idx-1)
        return result

print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))
print(Solution().smallerNumbersThanCurrent([6,5,4,8]))
print(Solution().smallerNumbersThanCurrent([7,7,7,7]))