from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i] % 2 == 0:
                i += 1
            elif nums[j] % 2 != 0:
                j-=1
            else:
                nums[i], nums[j] = nums[j], nums[i]

        return nums

print(Solution().sortArrayByParity(nums = [0,1,2]))
print(Solution().sortArrayByParity(nums = [3,1,2,4]))
print(Solution().sortArrayByParity(nums = [0,1]))
