from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0
        j = 1

        for i in range(0, len(nums), 2):
            if nums[i] % 2 == 1:
                while nums[j] % 2 == 1:
                    j += 2

                nums[i], nums[j] = nums[j], nums[i]
        return nums

print(Solution().sortArrayByParityII([4,2,5,7]))