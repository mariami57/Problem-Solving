from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1

        while i <= j:
            if i == j:
                nums[i] = nums[i] ** 2
            else:
                nums[i] = nums[i] ** 2
                nums[j]  = nums[j] ** 2

            i += 1
            j -= 1


        sorted_nums = sorted(nums)

        return sorted_nums

print(Solution().sortedSquares(nums = [-7,-3,2,3,11]))
print(Solution().sortedSquares(nums = [-4,-1,0,3,10]))