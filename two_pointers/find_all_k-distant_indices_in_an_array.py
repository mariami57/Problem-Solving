from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = []
        for i in range(len(nums)):
                for j in range(len(nums)):
                        if nums[j] == key and  abs(i - j) <= k:
                            result.append(i)
                            break

        return result

print(Solution().findKDistantIndices(nums = [2,2,2,2,2], key = 2, k = 2))
print(Solution().findKDistantIndices(nums = [3,4,9,1,3,9,5], key = 9, k = 1))



