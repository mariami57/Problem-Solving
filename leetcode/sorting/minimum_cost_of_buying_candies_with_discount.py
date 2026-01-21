from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        min_cost = 0
        count = 0
        for i in range(len(cost)-1, -1, -1):
            if count == 2 and len(cost) > 2:
                count = 0
                continue
            min_cost += cost[i]
            count += 1
        return min_cost
print(Solution().minimumCost([3,3,3,1]))
print(Solution().minimumCost([5,5]))
print(Solution().minimumCost([6,5,7,9,2,2]))
print(Solution().minimumCost([1,2,3]))

