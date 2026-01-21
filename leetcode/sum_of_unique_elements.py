from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        num_of_occurrences = {}
        for num in nums:
            num_of_occurrences[num] = num_of_occurrences.get(num, 0) + 1
        sum = 0
        for k in num_of_occurrences:
            if num_of_occurrences[k]==1:
                sum+=k
        return sum

nums = [1,2,3,4,5]
print(Solution().sumOfUnique(nums))