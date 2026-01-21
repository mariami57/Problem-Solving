from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = set(candyType)

        n_candies = len(candyType) // 2

        if len(types) <= n_candies:
            return len(types)
        return n_candies

print(Solution().distributeCandies([1,1,2,2,3,3]))
print(Solution().distributeCandies([1,1,2,3]))
print(Solution().distributeCandies([6,6,6,6]))